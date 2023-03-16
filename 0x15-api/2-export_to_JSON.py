#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    id = sys.argv[1]

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))

    employee_name = response.json()['name']

    tasks = []
    for task in todos.json():
        task_dict = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        tasks.append(task_dict)

    json_data = {id: tasks}
    with open("{}.json".format(id), "w") as json_file:
        json.dump(json_data, json_file)
