import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def scrape_matches(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    matches = []
    # Find the table with class 'zztable stats'
    table = soup.find("table", class_="zztable stats")
    if not table:
        print("No match table found.")
        return matches
    for row in table.find_all("tr", class_="parent"):
        cols = row.find_all("td")
        if len(cols) >= 10:
            date = cols[1].get_text(strip=True)
            time = cols[2].get_text(strip=True)
            home_away = cols[3].get_text(strip=True)
            opponent = cols[5].get_text(strip=True)
            matches.append({
                "date": date,
                "time": time,
                "home_away": home_away,
                "opponent": opponent
            })
    return matches
