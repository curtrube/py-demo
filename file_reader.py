# filename = "pi_digits.txt"
from cmath import pi


filename = "pi_million_digits.txt"
birthday = "09271992"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

# print(pi_string[:52])
# print(len(pi_string))

if birthday in pi_string:
    print("HooRay! Your birthday is in the first million digits of Pi")
else:
    print("Sorry, your birthday is not the first million digits of Pi")
