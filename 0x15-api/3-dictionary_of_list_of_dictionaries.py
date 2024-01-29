#!/usr/bin/python3

"""
  Get the data from an api using requests module
"""

import json
import requests
import sys

url_users = "https://jsonplaceholder.typicode.com/users"
url_todos = "https://jsonplaceholder.typicode.com/todos?userId="


def get_all_employers():
    users = requests.get(url_users).json()
    user_ids_names = []
    user_final_data = {}
    for user in users:
        user_final_data[user.get('id')] = []
        user_ids_names.append(
            {"id": user.get('id'), "username": user.get('username')})

    for user_id in user_ids_names:
        username = user_id['username']
        todos = requests.get("{}{}".format(url_todos, user_id["id"]))
        for todo in todos.json():
            todo_to_append = {"username": username, "task": todo.get(
                'title'), "completed": todo.get('completed')}
            user_final_data[todo.get('userId')].append(todo_to_append)

        with open("todo_all_employees.json", 'w') as f:
            json.dump(user_final_data, f)


if __name__ == "__main__":
    get_all_employers()
