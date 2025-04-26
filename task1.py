

try:
    with open("sample.txt","r") as file:
        for line in file:
            print(line,end="")
except FileNotFoundError:
    print("The file sample.txt doesn't exist")

