# zerozero2gcal ⚽📅

Import your football fixtures from [zerozero.pt](https://www.zerozero.pt) into Google Calendar.  
Run it once at the start of the season — all matches are created as events.  

---

## ✨ Features
- Scrapes all season fixtures from ZeroZero
- Creates Google Calendar events for each match
- One-time import: run once, and you're set
- Minimal setup required

---

## 🚀 Setup

### 1. Clone repository
```bash
git clone https://github.com/sousa16/zerozero2gcal.git
cd zerozero2gcal

```

### 2. Google Calendar Authentication

To set up Google Calendar authentication, follow the official Google Calendar API Python Quickstart guide:

https://developers.google.com/workspace/calendar/api/quickstart/python

Follow the steps in the link above to:
- Enable the Google Calendar API in your Google Cloud project
- Configure the OAuth consent screen
- Create OAuth 2.0 credentials for a Desktop app
- Download the `credentials.json` file and place it in your project root

The authentication logic in this project matches the Quickstart sample. On first run, you will be prompted to authenticate with your Google account, and a `token.json` file will be created for future use.

