filenames = ["cats.txt", "mypets.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            file_contents = f.read()

    except FileNotFoundError:
        # print(f"Error: {filename} does not exist.")
        pass

    else:
        print(file_contents)