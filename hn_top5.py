#!/usr/bin/env python3
"""Fetch and display the top 5 current Hacker News stories."""

import json
import urllib.request
import urllib.error


HN_API_BASE = "https://hacker-news.firebaseio.com/v0"


def fetch_json(url):
    """Fetch JSON data from a URL."""
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def get_top_story_ids():
    """Get the list of top story IDs from Hacker News."""
    url = f"{HN_API_BASE}/topstories.json"
    return fetch_json(url)


def get_story(story_id):
    """Get story details by ID."""
    url = f"{HN_API_BASE}/item/{story_id}.json"
    return fetch_json(url)


def main():
    """Fetch and print the top 5 Hacker News stories."""
    try:
        top_ids = get_top_story_ids()
        top_5_ids = top_ids[:5]

        print("Top 5 Hacker News Stories:\n")

        for i, story_id in enumerate(top_5_ids, start=1):
            story = get_story(story_id)
            title = story.get("title", "No title")
            url = story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
            print(f"{i}. {title}")
            print(f"   {url}\n")

    except urllib.error.URLError as e:
        print(f"Network error: Unable to connect to Hacker News API. {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except json.JSONDecodeError:
        print("Error: Failed to parse response from Hacker News API.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
