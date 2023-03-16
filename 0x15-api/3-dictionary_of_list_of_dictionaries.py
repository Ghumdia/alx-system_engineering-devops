#!/usr/bin/python3
"""Returns to-do list information for all employees."""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    # Retrieve all employees from the API
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    employees = response.json()

    # Create a dictionary to store the employee tasks
    employee_tasks = {}
    for employee in employees:
        # Retrieve the TODO list for the employee
        id = employee['id']
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
        
        # Extract the necessary information from the API response
        employee_name = employee['name']
        tasks = []
        for todo in todos.json():
            # Extract information from todo item
            task_completed = todo['completed']
            task_title = todo['title']
            
            # Add information to tasks list
            tasks.append({
                'username': employee_name,
                'task': task_title,
                'completed': task_completed
            })
        
        # Add tasks to employee_tasks dictionary
        employee_tasks[str(id)] = tasks
    
    # Export the data to a JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(employee_tasks, file)
    
    # Display success message
    print('Data successfully exported to {}'.format(filename))
