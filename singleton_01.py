# singleton in python
# since class and function are objects manipulated in python
# one ca define singleton as function

# Singleton definition
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()    
            return instances[cls]
    return getinstance

# Class definition with decorator
@singleton
class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1
# if  decoration not defined
# should add this after class definition
# Counter = singleton(Counter)

# Verify
print(type(Counter))    # <type 'classobj'> if no decoration
Counter = singleton(Counter)
print(type(Counter))    # <type 'function'>
print(Counter)    # <type 'function'>

count = Counter()
count.inc()

context(
arg1
arg2
arg3
)
ActisCommande('commande1', context)
ActisCommande('commande2', context)
run "function;arg1;arg2;arg3" in somepath
