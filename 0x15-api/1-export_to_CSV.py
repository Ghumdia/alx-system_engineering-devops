mport requests
import csv
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id = sys.argv[1]
    response = requests.get(url, params={'userId': employee_id})
    employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json().get('username')
    tasks = response.json()
    filename = employee_id + '.csv'

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })
