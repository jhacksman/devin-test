# Hacker News Top 5

A simple Python CLI tool that fetches and displays the top 5 current stories from Hacker News.

## Usage

```bash
python3 hn_top5.py
```

The script will output a numbered list of the top 5 stories with their titles and URLs.

## Example Output

```
Top 5 Hacker News Stories:

1. Example Story Title
   https://example.com/article

2. Another Story
   https://news.ycombinator.com/item?id=12345

...
```

## Requirements

Python 3.x (uses only standard library modules: `urllib` and `json`)

## Error Handling

The script handles network errors gracefully and will display a meaningful error message if it cannot connect to the Hacker News API.
