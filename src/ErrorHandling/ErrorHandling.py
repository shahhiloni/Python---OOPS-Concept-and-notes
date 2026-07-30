## in python we use methods for error  handling like try, except, else and finally blocks.

## try method for error handling 

# try: 
#   num = int(input ("Enter a number: "))
#   result = 10000/ num
#   print(result)

# except ZeroDivisionError:
#     print("cannot divide by zero")

# except ValueError: 
#    print("please enter valid integer")


## Cacheing  : except
   
# try: 
#    x = int("jgbjkbbu")

# except Exception as e:
#    print("error", e)


## else : 

# try: 
#    num = int(input("enter a number:"))
# except ValueError: 
#    print("invalid number")
# else: 
#    print("entered:", num)


## finally : use in file handling concept, use for execution
try: 
   file = open("data.txt", "r")
   print(file.read())

except FileNotFoundError: 
   print("file not found")

finally: 
   print("file execution completed")
   
