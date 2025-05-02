def count_languages(repos):
    # Dictionary to hold the count of each programming language
    counts = {}

    # Loop through each repository in the input list
    for repo in repos:
        # Safely get the language from the repo dictionary.
        # If 'language' is None or missing, default to 'Unknown'
        lang = repo.get('language') or 'Unknown'

        # Increment the count for this language.
        # If it's not in the dictionary yet, start at 0.
        counts[lang] = counts.get(lang, 0) + 1

    # Return the dictionary of language counts
    return counts
