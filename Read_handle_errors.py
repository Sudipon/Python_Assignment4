try:
    file1 = open('sample.txt', 'r')
    print("Reading file content:\n", file1.read())
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")