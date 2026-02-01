#!/usr/bin/env python3
"""
Hacker News Search CLI Tool

Searches Hacker News stories by keyword using the Algolia HN Search API.

Usage: python3 hn_search.py <keyword>
"""

import json
import sys
import urllib.error
import urllib.request
import urllib.parse


def search_hn(keyword):
    """Search Hacker News stories by keyword."""
    encoded_keyword = urllib.parse.quote(keyword)
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_keyword}&tags=story"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: Network error - {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Error: HTTP error {e.code} - {e.reason}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to parse API response", file=sys.stderr)
        sys.exit(1)
    except TimeoutError:
        print("Error: Request timed out", file=sys.stderr)
        sys.exit(1)
    
    return data.get('hits', [])


def display_results(results, limit=10):
    """Display search results."""
    if not results:
        print("No results found.")
        return
    
    for i, story in enumerate(results[:limit], 1):
        title = story.get('title', 'N/A')
        url = story.get('url') or f"https://news.ycombinator.com/item?id={story.get('objectID', '')}"
        points = story.get('points', 0)
        num_comments = story.get('num_comments', 0)
        
        print(f"{i}. {title}")
        print(f"   URL: {url}")
        print(f"   Points: {points} | Comments: {num_comments}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hn_search.py <keyword>", file=sys.stderr)
        print("Example: python3 hn_search.py 'rust'", file=sys.stderr)
        sys.exit(1)
    
    keyword = sys.argv[1]
    
    if not keyword.strip():
        print("Error: Keyword cannot be empty", file=sys.stderr)
        sys.exit(1)
    
    print(f"Searching Hacker News for: '{keyword}'\n")
    
    results = search_hn(keyword)
    display_results(results)


if __name__ == '__main__':
    main()
