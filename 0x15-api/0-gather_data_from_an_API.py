#!/usr/bin/python3
"""
place holder
"""


if __name__ == "__main__":

    import requests
    from sys import argv
    response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
    if response.status_code == 200:
        # Extract JSON data from the response
        data = response.json()

        # Get the list of completed tasks
        completed_tasks = [task for task in data if task['completed']]

        # Get the total number of tasks and the number of completed tasks
        total_tasks = len(data)
        completed_task_count = len(completed_tasks)

        # Get the employee name from the first task
        employee_name = data[0]['name']

        # Print the employee TODO list progress in the specified format
        print('Employee {} is done with tasks ({}/{}):'.format(
        employee_name, completed_task_count, total_tasks))
        for task in completed_tasks:
            print('\t {}'.format(task["title"]))
