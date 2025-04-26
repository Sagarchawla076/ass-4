


# 1. Take user input and write it to output.txt
user_input = input("Enter some text to write into the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# 2. Append additional data to the same file
additional_input = input("Enter some more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# 3. Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line,end="")
