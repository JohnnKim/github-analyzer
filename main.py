# main.py

import sys
from github_api import fetch_repos       # Function to fetch repositories from GitHub
from analysis import count_languages     # Function to count languages used across repos
from visualizer import pie_chart         # Function to visualize language usage as a pie chart

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]  # Extract the GitHub username from the command line

    try:
        # Fetch the user's repositories from GitHub
        repos = fetch_repos(username)

        # Analyze language usage across repositories
        lang_stats = count_languages(repos)

        # Print each repository and its language
        print("\n--- Repositories ---")
        for repo in repos:
            # If language is None, display as 'Unknown'
            print(f"{repo['name']}: {repo['language'] or 'Unknown'}")

        # Print summary statistics
        print("\n--- Summary ---")
        print(f"Total Repos: {len(repos)}")
        print("Languages Used:")
        for lang, count in lang_stats.items():
            print(f"- {lang}: {count} repos")

        # Generate a pie chart visualization of the language breakdown
        pie_chart(lang_stats)

    except Exception as e:
        # Catch and display any errors (e.g., bad username, API issues)
        print(f"Error: {e}")
        sys.exit(1)

# Run main() only if this file is executed directly
if __name__ == "__main__":
    main()
