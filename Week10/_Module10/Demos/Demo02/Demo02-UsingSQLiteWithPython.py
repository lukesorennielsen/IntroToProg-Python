import sqlite3  # this imports code from the sqlite module of PySQLite!

# TODO: Change the path to work on your computer.
DB_FILE_PATH: str = 'C:/Users/Admin/Documents/Python/sqlite/GPATracker.db'


# Functions ------------------------------------------
def create_connection(db_file):
    try:
        con = sqlite3.connect(db_file)  # This opens OR creates the database
        print('Connected! - SQLite Version is: ', sqlite3.version)
    except Exception:
        raise ConnectionError("Please check the path and file name.")
    return con


def select_student_data(connection: str):
    try:
        sql: str = f"SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA " \
                   f"FROM Students;"
        csr = connection.cursor()  # A cursor object allows you to submit commands
        csr.execute(sql)
        list_of_rows: list = csr.fetchall()  # fetchall puts all of the rows from the result into a list of tuples
        csr.close()  # Always close the cursor when your done
        return list_of_rows
    except Exception as e:
        raise sqlite3.OperationalError("Please check arguments for extra single quotes\n", e)


def insert_student_data(connection: str, id: int, first_name: str, last_name: str, gpa: str):
    try:
        sql: str = f"INSERT INTO Students (StudentFirstName, StudentLastName, StudentGPA) " \
                   f"VALUES ('{first_name}', '{last_name}', {gpa});"
        csr = connection.cursor()  # A cursor object allows you to submit commands
        csr.execute(sql)  # Single quotes for strings!
        csr.execute("commit;")  # You need to add this when using PySQLite!
        csr.close()  # Always close the cursor when your done
    except Exception as e:
        raise sqlite3.OperationalError("Please check arguments for extra single quotes", e)


# Main body of the script ------------------------------------------
db_con = create_connection(db_file=DB_FILE_PATH)  # This opens the connection

# Read Data
try:
    for row in select_student_data(connection=db_con):
        print(type(row), row)
except Exception as e:
    print(e)

# Write Data
try:
    insert_student_data(connection=db_con, id=2, first_name='Sue', last_name='Jones', gpa=3.5)
except Exception as e:
    print(e)

# Read Data
try:
    for row in select_student_data(connection=db_con):
        print(row)
except Exception as e:
    print(e)

# Always close the connection when your done
db_con.close()



