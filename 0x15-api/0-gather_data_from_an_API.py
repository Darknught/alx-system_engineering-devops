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
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
