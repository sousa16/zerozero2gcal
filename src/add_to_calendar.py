from googleapiclient.discovery import build


def add_events_to_calendar(creds, events, color_id="7", calendar_id="primary"):
    service = build("calendar", "v3", credentials=creds)
    for event in events:
        gcal_event = {
            "summary": event["summary"],
            "start": {
                "dateTime": event["start"].isoformat(),
                "timeZone": "Europe/Lisbon"
            },
            "end": {
                "dateTime": event["end"].isoformat(),
                "timeZone": "Europe/Lisbon"
            },
            "colorId": color_id
        }
        service.events().insert(calendarId=calendar_id, body=gcal_event).execute()
        print(f"Added event: {event['summary']}")
