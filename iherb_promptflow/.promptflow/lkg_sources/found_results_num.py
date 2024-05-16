from promptflow import tool
import re

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(found_products):
    num_products = re.findall(r"'num_results'\:\s*(\d+)", str(found_products))
    if len(num_products) > 0:
        extracted_num = int(num_products[0])
        if extracted_num != 0:
            return 1
    return 0