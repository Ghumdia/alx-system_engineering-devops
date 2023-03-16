#!/usr/bin/python3
"""Script that exports data in the CSV format."""

import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        user_res = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
        todos_res = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': user_id})

        try:
            username = user_res.json()['username']
            todos = todos_res.json()
        except ValueError:
            print('Invalid JSON')
            sys.exit(1)

        with open('{}.csv'.format(user_id), mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for todo in todos:
                writer.writerow({
                    'USER_ID': user_id,
                    'USERNAME': username,
                    'TASK_COMPLETED_STATUS': str(todo['completed']),
                    'TASK_TITLE': todo['title']
                })
    else:
        print('Usage: {} USER_ID'.format(sys.argv[0]))

