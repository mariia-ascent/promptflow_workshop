from promptflow import tool
import re

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(classification: str):
    number = re.findall('\d+', classification)
    if len(number) > 0:
        selected_option = int(number[0])
        return selected_option
    return 0