# Claude Auth

---

## How Claude CLI Authentication Works

### The Two Credential Types

There are two completely separate ways to authorize Claude Code to use
Anthropic's models. They work differently and bill differently.

**API Key (`ANTHROPIC_API_KEY`)**

Think of this like a hotel key card. Whoever has it gets in. No
questions asked about who they are. You create an API key once on
`console.anthropic.com`, copy it, and any program that sends it in a
request header gets billed to your Console account. The key itself is
the proof of authorization. There is no identity behind it — just a
secret string.

```
Your code → sends ANTHROPIC_API_KEY in X-Api-Key header → Anthropic API
→ Anthropic looks up the key → bills the linked Console account
→ returns the model response
```

This is why `claude -p "say hi"` works with just an API key — it is a
direct API call. No identity check. Just a key.

**OAuth Subscription Token (`CLAUDE_CODE_OAUTH_TOKEN`)**

This is tied to your personal Anthropic account (your email/login).
It proves who you are, not just that you have a secret. It bills
against your Pro/Max plan quota rather than charging per token. This
is what the interactive REPL requires.

---

### The Browser Dance — What Is Actually Happening

When you run `claude auth login`, this is the OAuth 2.0 Authorization
Code flow. Here is what happens step by step:

```
Step 1: claude CLI generates a random "state" string and a "code
        verifier" (a long random value for security)

Step 2: claude CLI opens your browser to:
        https://claude.ai/oauth/authorize?
          client_id=claude-code
          redirect_uri=http://localhost:PORT/callback
          response_type=code
          state=RANDOM_VALUE
          code_challenge=HASH_OF_VERIFIER

Step 3: You log in to claude.ai in the browser (or are already logged in)
        claude.ai verifies your identity (email + password or Google/GitHub SSO)

Step 4: claude.ai redirects your browser to:
        http://localhost:PORT/callback?code=AUTH_CODE&state=RANDOM_VALUE

Step 5: The claude CLI has been listening on localhost:PORT
        It receives the AUTH_CODE from the redirect

Step 6: claude CLI sends the AUTH_CODE + code_verifier to Anthropic's
        token endpoint to exchange for an access token

Step 7: Anthropic returns an access token (short-lived, ~1 hour)
        and a refresh token (long-lived, ~1 year)
        These are written to ~/.claude/.credentials.json

Step 8: All future requests use the access token as:
        Authorization: Bearer ACCESS_TOKEN
        When the access token expires, the refresh token silently
        gets a new one without any browser interaction
```

The "copy-paste mechanics" you hit in WSL happen at Step 4-5. The
browser redirect goes to `localhost:PORT` but that port is inside WSL's
network namespace, not Windows. The browser (running on Windows) cannot
reach `localhost:PORT` inside WSL. So the flow breaks. The workaround
is `claude setup-token`, which generates a long-lived token once on a
machine where the browser can reach localhost, then lets you use that
token as an env var on any machine — including WSL.

---

### How Code/Agents Use the Subscription Token Budget

When `CLAUDE_CODE_OAUTH_TOKEN` is set, every API call includes:

```
Authorization: Bearer sk-ant-oat01-...
```

Anthropic's backend resolves this token to your account, checks your
subscription tier (Pro/Max), and applies rate limits accordingly:

- **Pro plan**: ~5x usage limit vs free, shared across all Claude
  products (claude.ai chat, Claude Code, API calls with this token)
- **Max plan**: higher multiplier, priority access

The token budget is not a fixed number of tokens. It is a rate limit —
requests per minute and tokens per minute — that resets periodically.
If you hit the limit, Anthropic returns a 429 (rate limit) response and
claude CLI retries with exponential backoff.

Agents running in GitHub Actions use `CLAUDE_CODE_OAUTH_TOKEN` the same
way — the runner sets it as an environment variable and every Claude
subprocess picks it up. The budget comes from the account that generated
the token, which is why a shared token lets a whole course share one
plan's quota.

---

## Summary

| Question | Short Answer |
|---|---|
| How does OAuth token auth work? | Browser-based identity proof that writes credentials to disk — any process that reads the file is authorized |
| Why does WSL break the browser flow? | Browser runs on Windows, CLI runs in WSL — the localhost redirect cannot cross that boundary |
| How does subscription billing work? | Token ties to your account; Anthropic enforces rate limits per plan tier |
