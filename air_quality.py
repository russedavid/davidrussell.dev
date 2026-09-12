"""Air-quality lookups, kept separate from the site's rendering code."""

from collections import Counter, defaultdict
import math

import requests


def calculate_aqi_stats(hours_info):
    readings, dominant, concentrations = [], Counter(), defaultdict(list)
    for hour in hours_info:
        for index in hour.get("indexes", []):
            if "aqi" in index:
                readings.append(index["aqi"])
            if pollutant := index.get("dominantPollutant"):
                dominant[pollutant] += 1
        for pollutant in hour.get("pollutants", []):
            if pollutant.get("code") and "value" in pollutant.get("concentration", {}):
                concentrations[pollutant["code"]].append(pollutant["concentration"]["value"])
    return {
        "average_aqi": sum(readings) / len(readings) if readings else None,
        "dominant_pollutant": dominant.most_common(1),
        "pollutant_averages": {key: sum(values) / len(values) for key, values in concentrations.items()},
    }


def fetch_aqi_data(api_key, lat, lon):
    url = "https://airquality.googleapis.com/v1/history:lookup"
    payload = {
        "hours": 720,
        "location": {"latitude": lat, "longitude": lon},
        "pageSize": 100,
        "extraComputations": ["POLLUTANT_CONCENTRATION"],
    }
    hours, seen_tokens = [], set()
    for _ in range(20):
        try:
            response = requests.post(url, params={"key": api_key}, json=payload, timeout=(5, 15))
            response.raise_for_status()
            data = response.json()
        except requests.RequestException:
            # Request exception strings can include the URL and the visitor's key.
            raise ValueError("The air-quality service could not complete this lookup. Check your key and try again.") from None
        except ValueError:
            raise ValueError("The air-quality service returned an unreadable response.") from None
        if not isinstance(data, dict) or "error" in data:
            raise ValueError("The air-quality service rejected this lookup. Check your key and coordinates.")
        hours.extend(data.get("hoursInfo", []))
        token = data.get("nextPageToken")
        if not token:
            return calculate_aqi_stats(hours)
        if token in seen_tokens:
            raise ValueError("The air-quality service repeated a page. Try again later.")
        seen_tokens.add(token)
        payload["pageToken"] = token
    raise ValueError("The air-quality response exceeded the lookup limit. Try again later.")


def handle_aqi_request(api_key, coordinates_text):
    results = []
    for line in coordinates_text.splitlines():
        if not line.strip():
            continue
        try:
            lat, lon = map(float, line.strip().split(","))
            if not all(map(math.isfinite, (lat, lon))) or not (-90 <= lat <= 90 and -180 <= lon <= 180):
                raise ValueError
        except ValueError:
            results.append({"coordinates": (line.strip(),), "error": "Use latitude,longitude: latitude -90 to 90, longitude -180 to 180."})
            continue
        try:
            results.append({"coordinates": (lat, lon), "data": fetch_aqi_data(api_key, lat, lon)})
        except ValueError as error:
            results.append({"coordinates": (lat, lon), "error": str(error)})
    return results
