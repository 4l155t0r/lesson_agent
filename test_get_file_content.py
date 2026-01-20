from functions import get_file_content

arg_1 = "calculator"

arg_2_test_1 = "main.py"
arg_2_test_2 = "pkg/calculator.py"
arg_2_test_3 = "/bin/cat"
arg_2_test_4 = "pkg/does_not_exist.py"


print(f"Result for '{arg_2_test_1}' directory:")
test = get_file_content.get_file_content(arg_1, arg_2_test_1)
if test != 0:
    print(test)
else:
    print(len(test))
print("")

print(f"Result for '{arg_2_test_2}' directory:")
test = get_file_content.get_file_content(arg_1, arg_2_test_2)
if test != 0:
    print(test)
else:
    print(len(test))
print("")

print(f"Result for '{arg_2_test_3}' directory:")
test = get_file_content.get_file_content(arg_1, arg_2_test_3)
if test != 0:
    print(test)
else:
    print(len(test))
print("")

print(f"Result for '{arg_2_test_4}' directory:")
test = get_file_content.get_file_content(arg_1, arg_2_test_4)
if test != 0:
    print(test)
else:
    print(len(test))
print("")

