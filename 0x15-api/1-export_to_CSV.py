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
    - Exports data in CSV format with the specified format
    - File name must be: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Prepare data for CSV
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for todo in todos:
        csv_data.append([sys.argv[1], user.get("name"), str(
            todo.get("completed")), todo.get("title")])

    # Export data to CSV
    with open(f"{sys.argv[1]}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(csv_data)
