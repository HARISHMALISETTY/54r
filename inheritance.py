# class Parent:
#     def Pmethod(self):
#         print("iam a method from parent class")
#     def Pmethod2(self):
#         print("iam a method2 from parent class")

# class Child(Parent):
#     def Cmethod(self): 
#         super().Pmethod2()  # for accessing methods from     
#         print("iam a method from child class")

# obj1=Child()
# obj1.Pmethod2()

# class Chiranjeevi:
#     def C_assets(self):
#         self.c_worth=100
#         print(f"chiranjeevi assets-{self.c_worth} cr")

# class RamCharan(Chiranjeevi):
#     def R_assets(self):
#         self.r_worth=50
#         print(f"ram charan- worth {self.r_worth} cr")
#     def Total_assets(self):
#         super().C_assets()
#         total_worth=self.r_worth+self.c_worth
#         print(f"{total_worth}cr")

# rc_obj=RamCharan()
# rc_obj.R_assets()
# rc_obj.C_assets()
# rc_obj.Total_assets()

# class ParentActor:
#     def __init__(self,Pname,Pworth):
#         self.Pname=Pname
#         self.Pworth=Pworth
#         print(f"{self.Pname} is the parent")
#     def Passets(self):
#         print(f"{self.Pname} assets are {self.Pworth} cr")
# class ChildActor(ParentActor):    
#     def __init__(self,Pname,Cname,Pworth,Cworth):
#         super().__init__(Pname,Pworth)
#         self.Cname=Cname
#         self.Cworth=Cworth
#         print(f"{self.Cname}is came by the referrence of{self.Pname}")
#     def Cassets(self):
#         print(f"{self.Cname}is having worth of {self.Cworth}cr")
#     def TotalAssets(self):
#         print(f"total assets of {self.Cname} is {self.Pworth+self.Cworth}")
# class grandChildActor(ChildActor):
#     def __init__(self,Gname,Pname,Cname,Pworth,Cworth,Gworth):
#         self.Gname=Gname
#         self.Gworth=Gworth
#         super().__init__(Pname,Cname,Pworth,Cworth)
#     def Gassets(self):
#         print(f"{self.Gname} is having assets of {self.Gworth}")
#     def GTotalAssets(self):
#         print(f"{self.Gname}is having total assets of {self.Pworth+self.Cworth+self.Gworth}")

# gowtham=grandChildActor(Gname='gowtham',Cname='Mahesh',Pname='krishna',Cworth=50,Gworth=25,Pworth=100)
# gowtham.GTotalAssets()
# ramcharan=ChildActor("chiranjeevi","ramcharan",100)
# ramcharan.Cassets(75)
# ramcharan.TotalAssets()
# ramcharan.Passets()

# class MegaStar:
#     def __init__(self,M_Worth):
#         self.M_Worth=M_Worth
#         print(f"megastar having worth of{self.M_Worth}cr")
# class PowerStar:
#     def __init__(self,P_Worth):
#         self.P_Worth=P_Worth
#         print(f"powerstar having worth of{self.P_Worth}cr")
# class MegaPowerStar(MegaStar,PowerStar):
#     def __init__(self,Mp_Worth,M_Worth,P_Worth):
#        self.Mp_Worth=Mp_Worth      
#        MegaStar.__init__(self,M_Worth)
#        PowerStar.__init__(self,P_Worth)
#     def getMegaPowerStarAssets(self):
#         print(f"{self.Mp_Worth}")
#     def TotalAssets(self):
#         print(f"RAM CHARAN HAVING OVERALL OF {self.M_Worth+self.Mp_Worth+self.P_Worth} cr")
# rc=MegaPowerStar(Mp_Worth=150,M_Worth=100,P_Worth=100)
# rc.getMegaPowerStarAssets()
# rc.TotalAssets()




#method overriding--> replacing or changing the logic of method from superclass in subclass is called method overriding.
#method overriding can be applicable only when inheritance happens otherwise it won't applicable.

class Vehicle:
    def speed(self):
        print("vehicle speed is normal")
class Car(Vehicle):
    def speed(self):
        print("car speed is 120kmph")
class Cycle(Vehicle):
    def speed(self):
        print("cycle speed is 20kmph")
car=Car()
cycle=Cycle()

car.speed()
cycle.speed()