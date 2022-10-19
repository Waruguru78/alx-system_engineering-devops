#!/usr/bin/python3
"""module returns all the tasks and saves to json file"""
import json
import requests


if __name__ == "__main__":

    users_response = requests.get(
            "https://jsonplaceholder.typicode.com/users"
            )
    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos"
            )

    users = users_response.json()
    todos = todos_response.json()

    task_lists = []
    all_todos = {}

    for user in users:
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')
                             }
                task_lists.append(task_dict)
            all_todos[user.get('id')] = task_lists

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_todos, file)
           