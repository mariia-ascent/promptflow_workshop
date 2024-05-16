from promptflow import tool
import pyodbc

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def querying(generated_sql: str) -> str:
    try:
        # Check if the generated_sql contains the expected '```sql' delimiters
        if '```sql' in generated_sql and '```' in generated_sql.split('```sql')[1]:
            sql = generated_sql.split('```sql')[1].split('```')[0].replace(r'\n', '')
        else:
            return {"result": [], "num_results": 0, "error": "Invalid SQL format"}
        
        # Check if SQL query is not empty
        if sql:
            try:
                # Connect to Azure SQL database
                server = 'tcp:promptflowpoc.database.windows.net'
                database = 'prompt-flow-workshop'
                username = 'test'
                password = ' Tyrannausaurus_1234!'
                driver = '{ODBC Driver 17 for SQL Server}'
                conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
                
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()

                # Close connection
                cursor.close()
                conn.close()
                
                return {"result": rows, "num_results": len(rows)}
            
            except Exception as e:
                # Return 0 results if any error occurs
                return {"result": [], "num_results": 0, "error": str(e)}
        else:
            return {"result": [], "num_results": 0, "error": "No SQL query provided"}

    except IndexError as e:
        return {"result": [], "num_results": 0, "error": "Invalid SQL format: " + str(e)}

    except Exception as e:
        return {"result": [], "num_results": 0, "error": "An unexpected error occurred: " + str(e)}
