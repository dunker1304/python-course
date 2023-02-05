# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.print("Hello world")
class animal():
    def __init__(self):
        print('inittt')
    def eat(self):
        print('eatt')
        
class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print('doggg')

    def __str__(self):
      return "magic method"
        
        
<!-- # a = animal() -->
b = dog()

b.eat()

str(b)

# Remember magic/dunder methods