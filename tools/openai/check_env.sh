#!/usr/bin/env bash

if [ -z "$OPENAI_API_KEY" ]; then
  echo "❌ OPENAI_API_KEY not set"
  exit 1
else
  echo "✅ OPENAI API key detected"
fi
