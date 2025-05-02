# Repo Analyzer Bot

A Python tool that analyzes a GitHub user's repositories to summarize language usage and display visual insights.

## Features

Fetches public repositories using the GitHub API
Summarizes the number of repos per language
Visualizes language distribution with a pie chart

## Project Structure

```
repo-analyzer/
├── main.py            # Entry point
├── github_api.py      # GitHub data fetching
├── analysis.py        # Language counting logic
├── visualizer.py      # Pie chart generation
├── README.md          # This file
└── requirements.txt   # Dependencies
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py <github-username>
```

Example:

```bash
python main.py torvalds
```

## Requirements

* Python 3.7+
* Internet connection (to access the GitHub API)

## Notes

* Only public repositories are analyzed
* You can modify `visualizer.py` to add more chart types

## Author

John Kim — 2025
