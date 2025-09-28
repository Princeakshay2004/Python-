# Runtime Polymorphism 

class Mobiles:
    def features(self):
        print(" Calling To Person")
    
class Iphone(Mobiles):
    def features(self):
        super().features()           # Calling Super Method
        print (" Picture Quality")
        print()
      


class Samsung(Mobiles):
    def features(self):
        super().features()           # Calling Super Method
        print (" Os Power")
        print()

class Vivo(Mobiles):
    def features(self):
        super().features()           # Calling Super Method
        print (" Best Performance")
        print()




obj1=Iphone()
obj1.features()


obj2=Samsung()
obj2.features()


obj3=Vivo() 
obj3.features()
