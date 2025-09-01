from gcal_auth import get_credentials
from scraper import scrape_matches
from gcal_create_events import create_gcal_events
from add_to_calendar import add_events_to_calendar

# Authenticate and get Google Calendar API credentials
creds = get_credentials()

url = "https://www.zerozero.pt/equipa/tecnico-fc/323311/jogos"

# Get matches from zerozero
matches = scrape_matches(url)

# Create Google Calendar event objects
calendar_events = create_gcal_events(matches)

# Add events to Google Calendar with color
add_events_to_calendar(creds, calendar_events, color_id="7")
