#python, 주문 Input X version
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
        print("사장: 서빙담당에게 "+ str(Waiter.pass_money) +" 원 전달받기")
        Owner.revenue += Waiter.pass_money
        
    def give_salary(self):
        Owner.money -= ((Employee.num_Chef + Employee.num_Waiter)*Employee.salary)
        print("사장: 일급주기")
        
    def check_money(self):
        print(Owner.money + Owner.revenue)


class Customer(Person):
    menu = {"정식":5000, "특식":7000, "콜라":2000, "사이다":2000}
    def __init__(self, name, age):
        super().__init__(name, age)
        self.pay = 0
        print("배가 고픈 " + self.name+ " 입니다.")
        
    def order(self,a, Waiter, Chef):
        for i in a:
            print(self.name+" : "+str(i[0])+" "+str(i[1])+" 개 주세요!")
            self.pay += (int(Customer.menu[i[0]])*int(i[1]))
        Waiter.get_order(a)
        Chef.cook(a)
        Waiter.serving(a)

    def payment(self, Waiter):
        print(self.name+" 손님 "+str(self.pay)+"원 지불 완료")
        Waiter.pass_on_money(self.pay)
        
        
class Employee(Person):
    num_Chef = 0 
    num_Waiter = 0
    salary = 50000

    def get_salary(self):
        print(str(self.name)+" 직원: "+str(Employee.salary) +" 원 일급받기")

class Chef(Employee):
    def __init__(self,name,age):
        super().__init__(name, age)
        Employee.num_Chef += 1
        print("안녕하세요 "+ str(self.name) +" 요리사 입니다.")
        
    def cook(self,m):
        for i in m:
            if i[0] in ["정식", "특식"]:
                print(self.name+" (요리담당): 서빙담당에게 주문지를 받아서 "+str(i[0])+" "+str(i[1])+" 개 요리하기")
        

class Waiter(Employee):
    pass_money = 0 
    def __init__(self, name, age):
        super().__init__(name, age)
        Employee.num_Waiter += 1
        print("안녕하세요 "+ str(self.name) +" 웨이터 입니다.")
        
    def get_order(self, m):
        for i in m:
            print(self.name+" (서빙담당): "+str(i[0])+" "+str(i[1])+" 개 주문 받았습니다!")

    def serving(self, m):
        for i in m:
            if i[0] in ["정식", "특식"]:
                print(self.name+" (서빙담당): "+str(i[0])+" "+str(i[1])+" 개 요리담당에게 음식 받아서 서빙하기")
            else:
                print(self.name+" (서빙담당): "+str(i[0])+" "+str(i[1])+" 개 서빙하기")
        
    def pass_on_money(self, pay):
        Waiter.pass_money += pay
        print(self.name+" (서빙담당): 손님에게 "+ str(pay) +"원 받기")


print("-------------- 사장님 생성 --------------")
a = Owner("곽예진", 22)

print("-------------- 직원 (서빙, 요리 1명씩) 생성 --------------")
b = Chef("나 요리잘함", 22)
c = Waiter("나 서빙잘함", 22)

print("-------------- 손님1 등장 --------------")
c1 = Customer("빛이 나는 솔로", 20)

print("-------------- 손님1 정식 1개, 사이다 1개 주문 --------------")
c1.order([["정식",1],["사이다",1]],c,b)

print("-------------- 손님1 계산 --------------")
c1.payment(c)

print("-------------- 손님2,3 등장 --------------")
c2 = Customer("여보",20)
c3 = Customer("자기",20)

print("-------------- 손님2,3 특식 2개, 콜라 2개 주문 --------------")
c2.order([["특식",2],["콜라",2]],c,b)

print("-------------- 손님2,3 계산 --------------")
c2.payment(c)

print("-------------- 3명으로 하루 장사 마감, 사장님 하루 수익 정산 및 종업원들에게 일급 지급 --------------")
a.make_money()
a.give_salary()
b.get_salary()
c.get_salary()

print("-------------- 장사를 마치고 사장이 가진 잔액 확인 --------------")
a.check_money()