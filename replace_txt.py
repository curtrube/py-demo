message = "i have a pet cat"
message = message.replace("cat", "dog")
print(message)

with open("learning_python.txt") as file_object:
    file_contents = file_object.read()

# replace `python` with `javascript`
print(file_contents.replace("python", "javascript"))
