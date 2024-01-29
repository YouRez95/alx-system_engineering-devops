#!/usr/bin/python3

"""
  Get the data from an api using requests module
"""

import json
import requests
import sys


def get_data_and_write_to_file_json(userId):
    """
        get data and write it to file json
    """
    username = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + userId)
    username_in_json = username.json()
    username_of_user = username_in_json.get("username")

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + userId)
    todos_in_json = todos.json()

    dict_for_data = {userId: []}
    for todo in todos_in_json:
        is_completed = todo.get('completed')
        todo_title = todo.get('title')
        dict_for_data[userId].append(
            {"task": todo_title, "completed": is_completed,
             "username": username_of_user})
        name_of_file = "{}.json".format(userId)
        with open(name_of_file, 'w') as f:
            json.dump(dict_for_data, f)


if __name__ == "__main__":
    get_data_and_write_to_file_json(sys.argv[1])
