try:
    file = open("File Operations\Demo.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
      print("Somthing Went Wrong ")