file1 = open('Output.txt', 'w')
write = input("Enter text to write to the file: ")
file1.write(write)
file1.write('\n')
print("Data successfully written to Output.txt.")
print("\n")
file1.close()

file1 = open('Output.txt', 'a')
append = input("Enter additional text to append: ")
file1.write(append)
print("Data successfully appended.")
print("\n")
file1.close()

file1 = open('Output.txt', 'r')
print("Final content of Output.txt:\n", file1.read())
file1.close()