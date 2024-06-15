#!/usr/bin/python3
import json
import requests

def fetch_data():
    # Fetch users and todos data
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    return users, todos

def main():
    users, todos = fetch_data()

    # Create a dictionary to hold all tasks for all employees
    all_tasks = {}

    # Create a dictionary of users for easy lookup
    users_dict = {user['id']: user['username'] for user in users}

    for todo in todos:
        user_id = todo['userId']
        if user_id not in all_tasks:
            all_tasks[user_id] = []

        task = {
            "username": users_dict[user_id],
            "task": todo['title'],
            "completed": todo['completed']
        }
        all_tasks[user_id].append(task)

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

if __name__ == "__main__":
    main()

