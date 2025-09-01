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

### 3. Install dependencies

Activate your Python virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 4. Scrape matches and create events

Run the main script to scrape fixtures and add them to your Google Calendar:

```bash
python src/main.py
```

This will:
- Scrape all matches from zerozero.pt
- Create Google Calendar event objects for each match
- Add events to your calendar with the specified color

### 6. Customization

- To change the event color, edit `color_id` in `src/main.py` or `src/add_to_calendar.py` (see [Google Calendar API colors](https://developers.google.com/workspace/calendar/api/v3/reference/colors)).
- To change the team or season, update the URL in `src/main.py`.

