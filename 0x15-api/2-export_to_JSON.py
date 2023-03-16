#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import json
import requests
import sys

if __name__ == '__main__':
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Retrieve the employee information and TODO list from the API
    id = sys.argv[1]
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'\
		.format(id))
    todos = requests.get('https://jsonplaceholder.typicode.com/\
			todos?userId={}'.format(id))

    # Extract the necessary information from the API response
    employee_name = response.json()['name']
    task_list = []
    for todo in todos.json():
        task_list.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        })

    # Write the task list to a JSON file
    filename = '{}.json'.format(id)
    with open(filename, mode='w') as file:
        json.dump({id: task_list}, file)
