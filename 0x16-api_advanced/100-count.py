#!/usr/bin/python3
"""
Module to count occurrences of keywords in hot articles from a subreddit.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively fetches hot articles from a subreddit and
    counts occurrences of keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        word_count (dict): Dictionary to store keyword occurrences.
        after (str): Pagination parameter for next set of results.

    Returns:
        None (Prints the sorted word occurrences).
    """
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom-User-Agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return  # Invalid subreddit, do nothing

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        title_words = post["data"]["title"].lower().split()

        for word in word_list:
            key = word.lower()
            word_count[key] += title_words.count(key)

    after = data.get("data", {}).get("after")
    if after:
        return count_words(subreddit, word_list, word_count, after)

    sorted_words = sorted(
        [(word, count) for word, count in word_count.items() if count > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_words:
        print(f"{word}: {count}")
