# Repo Analyzer Bot

A Python tool that analyzes a GitHub user's public repositories to summarize language usage and display visual insights.

## Features

- Fetches public repositories using the GitHub API  
- Summarizes the number of repositories per programming language  
- Visualizes language distribution with a pie chart  

## Project Structure

```
repo-analyzer/
├── main.py # Entry point of the application
├── github_api.py # Handles GitHub API requests
├── analysis.py # Counts language usage
├── visualizer.py # Generates pie chart visualizations
├── README.md # Project documentation
└── requirements.txt # List of dependencies
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
python main.py johnnkim
```

## Requirements

* Python 3.7+
* Internet connection (to access the GitHub API)

## Notes

* Only public repositories are analyzed
* You can modify `visualizer.py` to add more chart types

## Author

John Kim — 2025
