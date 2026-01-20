from functions import run_python_file
arg_1 = "calculator"

arg_2_test_1 = "main.py"
arg_2_test_2 = "main.py"
arg_2_test_3 = "tests.py"
arg_2_test_4 = "../main.py"
arg_2_test_5 = "nonexistent.py"
arg_2_test_6 = "lorem.txt"

arg_3_test_2 = ["3 + 5"]


print(f"Result for '{arg_2_test_1}' file:")
test = run_python_file.run_python_file(arg_1, arg_2_test_1)
print(test)
print("")

print(f"Result for '{arg_2_test_2}' file and arg '{arg_3_test_2}':")
test = run_python_file.run_python_file(arg_1, arg_2_test_2, arg_3_test_2)
print(test)
print("")

print(f"Result for '{arg_2_test_3}' file:")
test = run_python_file.run_python_file(arg_1, arg_2_test_3)
print(test)
print("")

print(f"Result for '{arg_2_test_4}' file:")
test = run_python_file.run_python_file(arg_1, arg_2_test_4)
print(test)
print("")

print(f"Result for '{arg_2_test_5}' file:")
test = run_python_file.run_python_file(arg_1, arg_2_test_5)
print(test)
print("")

print(f"Result for '{arg_2_test_6}' file:")
test = run_python_file.run_python_file(arg_1, arg_2_test_6)
print(test)
print("")