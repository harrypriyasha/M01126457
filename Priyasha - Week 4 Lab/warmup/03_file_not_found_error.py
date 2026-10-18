# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print('The file was not found')
