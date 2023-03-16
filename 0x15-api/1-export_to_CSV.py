#!/usr/bin/python3
"""Script that exports data in the CSV format."""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    tasks = requests.get(url + 'todos', params={'userId': user_id}).json()

    # Save data to CSV file
    with open('{}.csv'.format(user_id), mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user['username'], task['completed'],
                             task['title']])

