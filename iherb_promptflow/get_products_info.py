from promptflow import tool
import pyodbc

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool():

    # Database connection parameters
    driver = '{ODBC Driver 17 for SQL Server}'
    server = 'tcp:promptflowpoc.database.windows.net'
    database = 'prompt-flow-workshop'
    username = 'test'
    password = ' Tyrannausaurus_1234!'

    # Establish a connection
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()

    # SQL query to select all columns except 'P_url'
    # Assuming the other columns are Title, Price, Description, Ingredients based on previous examples
    query = "SELECT [Title], [Price], [Description], [Ingredients] FROM [iherb_products_short];"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the query
    results = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    return results