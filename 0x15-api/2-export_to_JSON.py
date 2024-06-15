import requests
import sys
import json

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
    
    # Prepare the data for JSON export
    json_data = {str(employee_id): []}
    for todo in todos:
        task_data = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        }
        json_data[str(employee_id)].append(task_data)
    
    # Write the data to a JSON file
    json_file = f"{employee_id}.json"
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(json_data, file)
    
    print(f"Data exported to {json_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

