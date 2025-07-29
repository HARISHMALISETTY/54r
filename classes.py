# class Application:
#     def __init__(self,name,color,category):
#         self.name=name
#         self.logo_clr=color
#         self.categroty= category  
#     def getAppInfo(self):
#         print(f"{self.name} {self.logo_clr} {self.categroty}") 

# instagram=Application("instagram","pink","socailmedia")
# instagram.getAppInfo()
# zomato=Application("zomato","red","food")
# zomato.getAppInfo()
# amazon=Application("amazon","brown","ecommerce")
# amazon.getAppInfo()

class BankAccount:
    def __init__(acnt,name,acnt_num,ifsc,branch,balnce):
        acnt.name=name
        acnt.num=acnt_num
        acnt.ifsc=ifsc
        acnt.branch=branch
        acnt.balance=balnce
    def deposit(acnt,d_amnt):
        acnt.balance+=d_amnt
    def withdrawl(acnt,w_amnt):
        acnt.balance-=w_amnt
    def BalnceCheck(acnt):
        print(f"{acnt.balance}")

eeswar_acnt=BankAccount("EESHWAR",478965124711,'SAMPLE1212','KPHB',10000)
eeswar_acnt.BalnceCheck()
eeswar_acnt.deposit(5000)
eeswar_acnt.BalnceCheck()
eeswar_acnt.withdrawl(2500)
eeswar_acnt.BalnceCheck()
