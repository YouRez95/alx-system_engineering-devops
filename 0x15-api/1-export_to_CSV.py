#!/usr/bin/python3

"""
  Get the data from an api using requests module
"""
import requests
import sys


def get_data_and_write_to_file(userId):
    username = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + userId)
    username_in_json = username.json()
    username_of_user = username_in_json.get("username")

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + userId)
    todos_in_json = todos.json()

    for todo in todos_in_json:
        is_completed = todo.get('completed')
        todo_title = todo.get('title')

        name_of_file = "{}.csv".format(userId)
        f = open(name_of_file, "a")
        f.write('"{}","{}","{}","{}"\n'.format(
            userId, username_of_user, is_completed, todo_title))


if __name__ == "__main__":
    get_data_and_write_to_file(sys.argv[1])
