# WAP to print the total amount using *args, and **kwargs




# def sum(*args):
#     s = 0
#     for i in args:
#         s+= i
#         print(s)

# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40)



# def sum(**kwargs):
#     sum = 0
#     for i in kwargs.values():
#         sum = sum + i
#         print(sum)

# sum(a=20,b=20)
# sum(a=10,b=20,c=30)
# sum(a=10,b=20,c=30,d=40)


def sum(*args):
    sum = 0
    for items in args:
        sum = sum + 1
        print(sum)

nums = [20 , 30]
sum(*nums)
