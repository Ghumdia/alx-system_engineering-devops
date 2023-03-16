#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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
    tasks = len(todos.json())
    d_tasks = len([todo for todo in todos.json() if todo['completed']])

    # Display the employee TODO list progress in the required format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, d_tasks, tasks))
    for todo in todos.json():
        if todo['completed']:
            print("\t {}".format(todo['title']))
