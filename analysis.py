def count_languages(repos):
    counts = {}
    for repo in repos:
        lang = repo['language'] or 'Unknown'
        counts[lang] = counts.get(lang, 0) + 1
    return counts