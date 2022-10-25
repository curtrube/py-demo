def count_words(filename):
    """Count approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

    else:
        words = contents.split()
        num_words = len(words)
        title = filename.split(".", 1)
        print(f"There are {num_words} words in {title[0].title()}")

filenames = [
    "alice_in_wonderland.txt", 
    "moby_dick.txt",
    "little_women.txt",
    "siddhartha.txt",
    ]

for filename in filenames:
    count_words(filename)