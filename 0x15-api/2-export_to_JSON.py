#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an
employee from a REST API.
It accepts an employee ID as input and prints the employee's name,
the number of completed tasks,
and the titles of the completed tasks. The script uses the requests
library to make HTTP GET requests
to the API and safely accesses dictionary values using the get method.

Usage:
    python script.py <employee_id>

Requirements:
    - The script must use the requests library to make HTTP requests.
    - It must accept an employee ID as a command-line argument.
    - The script should not be executed when imported as a module.
    - Records all tasks that are owned by this employee
    - Exports data in JSON format with the specified format
    - File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")  # correctly fetch the username
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Export data to CSV
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": todo.get(
            "title"), "completed": todo.get("completed"), "username": username}
            for todo in todos]}, jsonfile)
