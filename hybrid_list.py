import math
def identify(input_list):
    result=[]
    for item in input_list:
        if isinstance(item, int):
            if math.isqrt(item)**2==item:
                result.append(f"{item}#")
            else:
                result.append(f"{item}.")
        elif isinstance(item,float):
            result.append(f"{item}*")
    return result
user_input=input("Enter your choise:")
input_list=[]
for value in user_input.split():
    try:
        if '.' in value:
            input_list.append(float(value))
        else:
            input_list.append(int(value))
    except ValueError:
        print(f"Invalid input:{value}")
output= identify(input_list)
print(output)
