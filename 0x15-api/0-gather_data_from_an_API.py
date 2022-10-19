#!/usr/bin/python3
""" module sends request to an API """

import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/"
            )

    employee_name = user_response.json().get('name')
    completed_tasks = 0
    total_tasks = 0

    for task in todos_response.json():
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1

    todo_content = '\n'.join(["\t " + task.get('title')
                              for task in todos_response.json()
                              if task.get('userId') == int(employee_id)
                              and task.get('completed')])
    print(
            f"Employee {employee_name}",
            f"is done with ({completed_tasks}/{total_tasks})"
            )
    print(todo_content)
    