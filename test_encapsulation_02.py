# Remarks :
# Version before 2.2 : print should be print()
#!/usr/bin/env python
 
class Car:
 
    def __init__(self):
        self.__updateSoftware()
 
    def drive(self):
        print('driving')
 
    def __updateSoftware(self):
        print('updating software')
 
redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  # not accesible from object.
redcar._Car__updateSoftware()  # accesible from object.
# Modifs sur la Branch_1