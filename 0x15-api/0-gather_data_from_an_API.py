#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given
employee ID using a REST API.
"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    response = requests.get(user_url)
    if response.status_code != 200:
        sys.exit("Invalid Employee ID")

    employee_name = response.json().get("name", "Unknown")

    todo_url = f"{user_url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    done_tasks = [task["title"] for task in tasks if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks(
        {len(done_tasks)}/{len(tasks)}): ")
    for task in done_tasks:
        print(f"\t {task}")
