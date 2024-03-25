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
    - File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    # Export data to CSV
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{"username": user.get(
            "username"), "task": todo.get(
                "title"), "completed": todo.get("completed")}
            for todo in todos if todo.get("userId") == user.get(
                "id")] for user in users}, jsonfile)
