#!/usr/bin/python3
"""Returns the to-do lists of an employee"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
id = int(sys.argv[1])
user = requests.get(url + "users/{}".format(id)).json()
todos = requests.get(url + "todos", params={"userId": id}).json()

completed = [t.get("title") for t in todos if t.get("completed") is True]
print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
[print("\t {}".format(c)) for c in completed]
