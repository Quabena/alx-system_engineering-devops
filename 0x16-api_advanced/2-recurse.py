#!/usr/bin/python3
"""
Module to recursively query Reddit API for hot posts.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves all hot post titles from a given subreddit.
    Args:
        subreddit (str): The subreddit name.
        hot_list (list): A list to store post titles
        (default is an empty list).
        after (str): The pagination parameter for the next set of results.
    Returns:
        list: A list of hot post titles or None if subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom-User-Agent"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Append titles to the list
        hot_list.extend([post["data"].get("title") for post in posts])

        # Get the next page token
        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
