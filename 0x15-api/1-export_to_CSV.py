import requests
import sys
import csv

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
    
    # Prepare the data for CSV export
    csv_data = []
    for todo in todos:
        csv_data.append([employee_id, user['username'], todo['completed'], todo['title']])
    
    # Write the data to a CSV file
    csv_file = f"{employee_id}.csv"
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
    
    print(f"Data exported to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

