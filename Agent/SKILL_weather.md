---
name: weather-demo
description: retrieve current weather from the web and summarize it in a natural, human-like way. use when the user asks for weather, temperature, forecast, current conditions, rain chances, or local weather updates where freshness matters. this skill is for lightweight demo-style weather lookup using a simple web api rather than a formal weather platform integration.
---

# Weather Demo

Use this skill to gather current weather conditions from a simple public weather endpoint and turn them into a short, natural-language update.

## Retrieval command

When current weather is needed, build a location query from the user's city or place name and run:

```bash
curl -sL "https://wttr.in/<LOCATION>?format=j1"