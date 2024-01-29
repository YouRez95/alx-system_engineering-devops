#!/usr/bin/python3

"""
  Get the data from an api using requests module
"""
import requests
import sys


def get_data():
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1])
    user_in_json = user.json()
    name_of_user = user_in_json.get("name")

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1])
    todos_in_json = todos.json()

    todos_to_be_completed = 0
    todos_completed = 0
    todos_completed_title = []

    for todo in todos_in_json:
        todos_to_be_completed = todos_to_be_completed + 1
        is_completed = todo.get('completed')
        if is_completed is True:
            todos_completed_title.append(todo.get('title'))
            todos_completed = todos_completed + 1
    print("Employee {} is done with tasks({}/{}):".format(name_of_user,
          todos_completed, todos_to_be_completed))
    for task in todos_completed_title:
        print("\t {}".format(task))


if __name__ == "__main__":
    get_data()
