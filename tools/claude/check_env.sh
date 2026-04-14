#!/usr/bin/env bash

if [ -z "$CLAUDE_CODE_OAUTH_TOKEN" ]; then
  echo "❌ CLAUDE_CODE_OAUTH_TOKEN not set"
  exit 1
else
  echo "✅ CLAUDE CODE OAUTH TOKEN detected"
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo "❌ ANTHROPIC_API_KEY not set"
  exit 1
else
  echo "✅ ANTHROPIC API key detected"
fi
