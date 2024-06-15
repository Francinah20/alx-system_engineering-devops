import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch the user information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user = user_response.json()
    
    # Fetch the TODO list information
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Calculate the total number of tasks and the number of completed tasks
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    
    # Display the employee's TODO list progress
    print(f"Employee {user['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

