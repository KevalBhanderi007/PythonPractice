# class MyClass:
#     variable = 5415151511

#     def function(self):
#         print("This is a message inside the class.")


# obj1 = MyClass()
# obj2 = MyClass()
# obj3 = MyClass()
# obj4 = MyClass()
# obj5 = MyClass()

# print(MyClass.variable)

# obj1.variable = "jdxb,b m kdbkbk knbsdk sndj"

# print(obj1.variable)
# obj1.function()

# class NumberHolder:

#    def __init__(self, number):
#        self.number = number

#    def returnNumber(self):
#        return self.number

# var = NumberHolder(7)
# print(var.returnNumber()) 

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str

# car1 = Vehicle()
# car1.name = "maruti"
# car1.kind = "car"
# car1.color ="red"
# car1.value =1000000

# car1 = Vehicle()
# car1.name = "suzuki"
# car1.kind = "car"
# car1.color ="red"
# car1.value =400000

# car2 = Vehicle()
# car2.name = "ferrari"
# car2.kind = "car"
# car2.color ="red"
# car2.value =800000

# print(car1.description())
# print(car2.description())/


class bike:
     
     category = "vehicle"      

     def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year

    #  def show_info(self):
    #     #  return "%s %s %s" %  (self.brand,self.model,self.year)   
    #      return f"{self.year} {self.brand} {self.model}" 

bike1 = bike("honda","hero",2041)

bike1.brand = "suzuki"
      
bike2 = bike("bmw","slit",2561)
       
print(bike1.brand)       
print(bike2.year)  

