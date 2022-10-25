filename = "learning_python.txt"

print("1st")
with open(filename) as file_object:
    file_contents = file_object.read()
print(file_contents)

print("2nd")
with open(filename) as file_object:
    for line in file_object:
        print(line)

print("3rd")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
