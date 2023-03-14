#!/usr/bin/python3
"""
Returns the to-do lists of an employee
"""
import requests
import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_url = 'https://jsonplaceholder.typicode.com/users/'
        todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        NAME = requests.get(user_url + sys.argv[1]).json()['name']
        DONE_TASKS = len([task for task in requests.
                                    get(todo_url + sys.argv[1]).json()
                                    if task['completed'] is True])
        TASKS = len(requests.get(todo_url + sys.argv[1]).json())
        DONE_TASKS_TITLES = [task['title'] for task in requests.
                             get(todo_url + sys.argv[1]).json()
                             if task['completed'] is True]

        print('Employee {} is done with tasks({}/{}):'.
              format(NAME, DONE_TASKS,
                     TASKS))
        for TASK_TITLE in DONE_TASKS_TITLES:
            print('\t {}'.format(TASK_TITLE))
