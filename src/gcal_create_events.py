from datetime import datetime, timedelta


def create_gcal_events(matches):
    events = []
    for match in matches:
        # Format event name
        event_name = f"TFC vs {match['opponent']} {match['home_away']}"
        # Parse date and time
        dt_str = f"{match['date']} {match['time']}"
        try:
            start_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        except ValueError:
            # Fallback if time format is different
            start_dt = datetime.strptime(match['date'], "%Y-%m-%d")
        end_dt = start_dt + timedelta(hours=2)
        event = {
            "summary": event_name,
            "start": start_dt,
            "end": end_dt,
        }
        events.append(event)
    return events
