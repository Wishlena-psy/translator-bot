#!/bin/bash
if [ -f /home/agent/.agent/.env ]; then
  source /home/agent/.agent/.env
  export CLAUDE_CODE_OAUTH_TOKEN
fi
while IFS= read -r line || [ -n "$line" ]; do
  [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue
  export "$line"
done < /home/agent/projects/translator-bot/tr.env
while IFS= read -r line || [ -n "$line" ]; do
  [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue
  key="${line%%=*}"
  [ -z "${!key}" ] && export "$line"
done < /home/agent/projects/jarvis-content/config.env
exec node /home/agent/projects/translator-bot/bot.js
