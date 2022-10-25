filename = "moby_dick.txt"

with open(filename, encoding='utf-8') as f:
    file_contents = f.read()

print(file_contents.lower().count('the'))