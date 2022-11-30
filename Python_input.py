#python, 주문 Input version
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        pass
    
class Owner(Person):
    revenue = 0
    money = 1000000
    def __init__(self, name, age):
        super().__init__(name, age)
        print("안녕하세요 "+ str(self.name) +" 사장 입니다.")
        
    def make_money(self):
        print("사장: 서빙담당에게 돈 전달받기")
        
    def give_salary(self):
        print("사장: 일급주기")
        Owner.money -= ((Employee.num_Chef + Employee.num_Waiter)*Employee.salary)
        
    def check_money(self):
        print(Owner.money + Owner.revenue)


class Customer(Person):
    menu= {"정식":5000, "특식":7000, "콜라":2000, "사이다":2000}
    def __init__(self, name, age):
        super().__init__(name, age)
        self.pay = 0
        for i in self.name:
            print("배가 고픈 " + str(i)+ " 입니다.")
        
    def order(self):
        c = 1
        while int(c) != 0:
            a = input("손님, 음식은 뭘로 하시겠어요? ")
            b = input("몇 개 원하시나요? ")
            self.pay += (int(Customer.menu[a])*int(b))
            c = input("더 주문 하시겠어요? 네는 1, 아니요는 0으로 답해주세요 ")
        
    def payment(self):
        Owner.revenue += self.pay
        print(str(self.pay)+"원 지불 완료")
        

class Employee(Person):
    num_Chef = 0 
    num_Waiter = 0
    salary = 50000
    def get_salary(self):
        print("직원: 일급받기")

class Chef(Employee):
    def __init__(self,name,age):
        super().__init__(name, age)
        Employee.num_Chef += 1
        print("안녕하세요 "+ str(self.name) +" 요리사 입니다.")
        
    def cook(self):
        print("요리담당: 서빙담당에게 주문지를 받아서 해당되는 음식 요리하기")

class Waiter(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        Employee.num_Waiter += 1
        print("안녕하세요 "+ str(self.name) +" 웨이터 입니다.")
        
    def get_order(self):
        print("서빙담당: 손님에게 주문받아서 주문입력하고 주문지 요리담당에게 전달")
        
    def serving(self):
        print("서빙담당: 요리담당에게 음식 받아서 서빙하기")
        
    def pass_on_money(self):
        print("서빙담당: 손님에게서 돈받아서 식당 주인에게 전달")
        
print("-------------- 사장님 생성 --------------")
a = Owner("곽예진", 22)

print("-------------- 직원 (서빙, 요리 1명씩) 생성 --------------")
b = Chef("나 요리잘함", 22)
c = Waiter("나 서빙잘함", 22)

print("-------------- 손님1 등장 --------------")
c1 = Customer(["빛이 나는 솔로"], 20)

print("-------------- 손님1 정식 1개, 사이다 1개 주문 --------------")
c1.order()
c.get_order()
b.cook()
c.serving()

print("-------------- 손님1 계산 --------------")
c1.payment()
c.pass_on_money()
a.make_money()

print("-------------- 손님2,3 등장 --------------")
c23 = Customer(["여보","자기"],[20, 20])

print("-------------- 손님2,3 특식 2개, 콜라 2개 주문 --------------")
c23.order()
c.get_order()
b.cook()
c.serving()

print("-------------- 손님2,3 계산 --------------")
c23.payment()
c.pass_on_money()
a.make_money()

print("-------------- 3명으로 하루 장사 마감, 사장님 종업원들에게 일급 지급 --------------")
a.give_salary()
b.get_salary()
c.get_salary()

print("-------------- 장사를 마치고 사장이 가진 잔액 확인 --------------")
a.check_money()