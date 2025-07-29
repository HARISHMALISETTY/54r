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

class Chiranjeevi:
    def C_assets(self):
        self.c_worth=100
        print(f"chiranjeevi assets-{self.c_worth} cr")

class RamCharan(Chiranjeevi):
    def R_assets(self):
        self.r_worth=50
        print(f"ram charan- worth {self.r_worth} cr")
    def Total_assets(self):
        super().C_assets()
        total_worth=self.r_worth+self.c_worth
        print(f"{total_worth}cr")

rc_obj=RamCharan()
rc_obj.R_assets()
rc_obj.C_assets()
rc_obj.Total_assets()