# the try block lets you test a block of code for errors 
# the except block lets you handle the error
# the else block lets you execute code when there is error
# the finally block lets you execute code, regardless of result of the try and except block

# a=10
# try:
#     print(a)
# except:
#     print("variable should be given a value")

# try:
#     print(a)
# except:
#     print("variable should be given a value")
# else:
#     print("there is no any error")
# finally:
#     print("Done")

try:
    file =open("text.txt")
    try:
        file.seek(0)
        print(file.read())
    except:
        print("something went wrong")
    finally:
        print("Done successfully")
except:
    print("file didnot open or you have no such kind of file")