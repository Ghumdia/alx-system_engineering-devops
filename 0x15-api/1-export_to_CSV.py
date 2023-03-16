#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
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

    filename = '{}.csv'.format(id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for todo in todos.json():

            # Extract information from todo item
            task_completed = str(todo['completed'])
            task_title = todo['title']
            
            # Write information to CSV file
            writer.writerow([id, employee_name, task_completed, task_title])
