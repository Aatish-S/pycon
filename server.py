import psycopg2
import netcon

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="truecolors_print@yeet#4545",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="print_manager")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")