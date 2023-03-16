#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))

    # Extract the necessary information from the API response
    employee_name = response.json()['name']
    tasks = todos.json()
    tasks_list = []
    for task in tasks:
        task_dict = {
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
        }
        tasks_list.append(task_dict)

    # Export the employee TODO list in JSON format
    filename = '{}.json'.format(id)
    with open(filename, 'w') as f:
        json.dump({id: tasks_list}, f, indent=4)

    # Display the employee TODO list progress in the required format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, \
	len([task for task in tasks if task['completed']]), len(tasks)))
    for task in tasks:
        if task['completed']:
            print("\t{}".format(task['title']))
