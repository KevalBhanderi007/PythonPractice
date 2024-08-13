# def divider(a,b):
#    try:
#       ans = a/b
#       print(f"ans is {ans}")
#    except ZeroDivisionError:
#       print("this show an error") 

# divider(25,5)

# divider(96,7)

# divider(52,0)


# def show_num(mylist, index):
#    try :
#       value = mylist[index]
#       print(f"answer is {index}: {value}")
#    except IndexError:
#       print("this is an error")

# mylist = [2,3,2,6,58,99,4,326,4,994,9794,979442]  
# show_num(mylist,5) 

# show_num(mylist,20)


def readfile(filename):
    try:
      with open(filename,'r') as file:
           content = file.read()
           print(f" file content : {content}")
    except FileNotFoundError:
        print (f"this file {filename} not found")

readfile('package.txt')

readfile('mod.py')        

    