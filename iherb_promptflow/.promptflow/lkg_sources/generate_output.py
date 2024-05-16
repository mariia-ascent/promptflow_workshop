from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, input2: str, input3: str, input4: str,) -> str:
    inputs = [i for i in [input1, input2, input3, input4] if i is not None]
    # Join the filtered inputs with a separator, for example, a space
    result = ' '.join(inputs)
    return result