# main.py

import sys
from github_api import fetch_repos
from analysis import count_languages
from visualizer import pie_chart

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]

    try:
        repos = fetch_repos(username)
        lang_stats = count_languages(repos)

        print("\n--- Repositories ---")
        for repo in repos:
            print(f"{repo['name']}: {repo['language'] or 'Unknown'}")

        print("\n--- Summary ---")
        print(f"Total Repos: {len(repos)}")
        print("Languages Used:")
        for lang, count in lang_stats.items():
            print(f"- {lang}: {count} repos")

        pie_chart(lang_stats)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()