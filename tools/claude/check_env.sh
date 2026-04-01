#!/usr/bin/env bash

if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo "❌ ANTHROPIC_API_KEY not set"
  exit 1
else
  echo "✅ API key detected"
fi
