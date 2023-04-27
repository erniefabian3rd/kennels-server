import sqlite3
import json
from models import EmployeeAnimal

def get_all_employee_animals():
    """Gets all assignments for employees/animals"""
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            ea.id,
            ea.employee_id,
            ea.animal_id
        FROM EmployeeAnimal ea
        """)

        # Initialize an empty list to hold all employee_animal representations
        employee_animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee_animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # EmployeeAnimal class above.
            employee_animal = EmployeeAnimal(row['id'], row['employee_id'], row['animal_id'])

            employee_animals.append(employee_animal.__dict__)

    return employee_animals

def get_single_employee_animal(id):
    """Gets single employee_animal assignment"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            ea.id,
            ea.employee_id,
            ea.animal_id
        FROM EmployeeAnimal ea
        WHERE ea.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee_animal = EmployeeAnimal(data['id'], data['employee_id'], data['animal_id'])

        return employee_animal.__dict__