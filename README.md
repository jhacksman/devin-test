# devin-test

A collection of CLI tools for various tasks.

## Tools

### hn_search.py

A command-line tool to search Hacker News stories by keyword using the Algolia HN Search API.

**Usage:**
```bash
python3 hn_search.py <keyword>
```

**Example:**
```bash
python3 hn_search.py 'rust'
```

**Output:**
Displays the top 10 results with:
- Title
- URL
- Points
- Number of comments

**Requirements:**
- Python 3 (stdlib only - uses urllib, json, sys)

**Error Handling:**
- Missing arguments: Shows usage instructions
- Empty keyword: Shows error message
- Network errors: Displays connection error details
- No results: Shows "No results found" message
