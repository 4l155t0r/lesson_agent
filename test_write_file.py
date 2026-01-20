from functions import write_file

arg_1 = "calculator"

arg_2_test_1 = "lorem.txt"
arg_2_test_2 = "pkg/morelorem.txt"
arg_2_test_3 = "/tmp/temp.txt"

arg_3_test_1 = "wait, this isn't lorem ipsum"
arg_3_test_2 = "lorem ipsum dolor sit amet"
arg_3_test_3 = "this should not be allowed"


print(f"Result for '{arg_2_test_1}' file:")
test = write_file.write_file(arg_1, arg_2_test_1, arg_3_test_1)
print(test)
print("")


print(f"Result for '{arg_2_test_2}' file:")
test = write_file.write_file(arg_1, arg_2_test_2, arg_3_test_2)
print(test)
print("")


print(f"Result for '{arg_2_test_3}' file:")
test = write_file.write_file(arg_1, arg_2_test_3, arg_3_test_3)
print(test)
print("")
