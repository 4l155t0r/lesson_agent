from functions import get_files_info

arg_1 = "calculator"

arg_2_test_1 = "."
arg_2_test_2 = "pkg"
arg_2_test_3 = "/bin"
arg_2_test_4 = "../"

print(f"Result for '{arg_2_test_1}' directory:")
test_1 = get_files_info.get_files_info(arg_1, arg_2_test_1)
if test_1 != 0:
    print(test_1)
print("")

print(f"Result for '{arg_2_test_2}' directory:")
test_1 = get_files_info.get_files_info(arg_1, arg_2_test_2)
if test_1 != 0:
    print(test_1)
print("")

print(f"Result for '{arg_2_test_3}' directory:")
test_1 = get_files_info.get_files_info(arg_1, arg_2_test_3)
if test_1 != 0:
    print(test_1)
print("")

print(f"Result for '{arg_2_test_4}' directory:")
test_1 = get_files_info.get_files_info(arg_1, arg_2_test_4)
if test_1 != 0:
    print(test_1)
print("")

