---
name: google-news-demo
description: retrieve recent news from the web and summarize it in a natural, human-like way. use when the user asks for latest news, breaking news, current events, recent developments, trending stories, or updates on a topic where freshness matters. this skill is for lightweight demo-style news lookup using a shell command rather than a formal news api.
---

# Google News Demo

Use this skill to gather recent news headlines from the web and turn them into a short, natural-language update.

## Retrieval command

When recent news is needed, build a search query from the user's topic and run:

```bash
curl -sL "https://www.google.com/search?q=<QUERY>&tbm=nws" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
| grep -oP '(?<=<div class="BNeawe vvjwJb AP7Wnd">).*?(?=</div>)' \
| head -n 15


