def greeting():
    print(" sedbzj kfjbc kzefh kufheclni ghefouuon iugeoudbu ougeubu")

keval = "Genius and Good " 

# l = [ 8,4,9,6,14,18, 56, 85 ,89 ,33 ,99, 28,29]
# # for i in l:
# ans =list(filter(lambda x : (x % 2) == 0,l))
# print(ans)

# # lambda examples

# # Example using lambda with map() to square numbers in a list
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))

# print(squared)  # Output: [1, 4, 9, 16, 25]

def fl(pelo , bijo , trijo , *bakina):
    print(f"{pelo} chhe")
    print(f"{bijo} chhe")
    print(f"{trijo} chhe")
    print(f"{bakina} chhe")

fl(1,2,3,4,5,6,7,8,9)


def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")


