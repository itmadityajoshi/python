my_file=open("text.txt")
print(my_file)
my_file.seek(0)
print(my_file.read())

#readlines returns the number of lines in the text

my_file.seek(0)
print(my_file.readline())


my_file.seek(0)
print(my_file.readlines())

