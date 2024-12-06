import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

# Create the Employee table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT,
        Role TEXT,
        Salary REAL,
        ContactInfo TEXT
    )
''')
connection.commit()

# Function to add an employee record
def add_employee(emp_id, name, dept, role, salary, contact):
    cursor.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?)", 
                   (emp_id, name, dept, role, salary, contact))
    connection.commit()
    print("Employee added successfully!")

# Function to view all employee records
def view_employees():
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()
    if not employees:
        print("No employee records found.")
    else:
        for row in employees:
            print(row)

# Function to update an employee's salary
def update_employee(emp_id, new_salary):
    cursor.execute("UPDATE Employee SET Salary = ? WHERE EmployeeID = ?", (new_salary, emp_id))
    connection.commit()
    if cursor.rowcount == 0:
        print("Employee not found.")
    else:
        print("Employee salary updated successfully!")

# Function to delete an employee record
def delete_employee(emp_id):
    cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (emp_id,))
    connection.commit()
    if cursor.rowcount == 0:
        print("Employee not found.")
    else:
        print("Employee deleted successfully!")

# Main menu loop
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            role = input("Enter Role: ")
            salary = float(input("Enter Salary: "))
            contact = input("Enter Contact Info: ")
            add_employee(emp_id, name, dept, role, salary, contact)

        elif choice == '2':
            view_employees()

        elif choice == '3':
            emp_id = int(input("Enter Employee ID: "))
            new_salary = float(input("Enter New Salary: "))
            update_employee(emp_id, new_salary)

        elif choice == '4':
            emp_id = int(input("Enter Employee ID: "))
            delete_employee(emp_id)

        elif choice == '5':
            print("Exiting...")
            connection.close()
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
