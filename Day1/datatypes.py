var = int(input("Enter an integer: "))
print("You entered:", var)
float_var = float(input("Enter a float: "))
print("You entered:", float_var)
str_var = input("Enter a string: ")
print("You entered:", str_var)
bool_var = input("Enter a boolean (True/False): ")
bool_var = bool_var.lower() in ['true', '1', 't', 'y', 'yes']
print("You entered:", bool_var)