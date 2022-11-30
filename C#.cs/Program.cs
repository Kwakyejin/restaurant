using System;
using System.Collections.Generic;

public class Person{
    protected string name;
    protected int age;
    public Person(string _name, int _age){
        name = _name;
        age = _age;
    }
   
    /**~Person(){
        System.Console.WriteLine("Instance removed");
    }**/
    /*소멸자 없어도 된다고 하셔서 주석 처리 하겠습니다.*/
}

public class Owner : Person{
    public static int money = 1000000;
    public static int revenue = 0;
    public Owner(string _name, int _age) : base(_name, _age){
        System.Console.WriteLine("안녕하세요 "+ name +" 사장 입니다.");
    }
    public void make_money(){
        System.Console.WriteLine("사장: 서빙담당에게 "+ Waiter.pass_money +" 원 전달 받기");
        revenue += Waiter.pass_money;
    }
    public void give_salary(){
        System.Console.WriteLine("사장: 일급주기");
        money -= ((Employee.num_Chef+Employee.num_Waiter))*Employee.salary;
    }
    public void check_money(){
        System.Console.WriteLine(money + revenue);
}
}
public class Customer : Person{
    private int pay = 0;
    public static Dictionary<string, int> menu = new Dictionary<string, int>(){
        {"정식",5000}, {"특식",7000}, {"콜라",2000}, {"사이다",2000}
    };
    public Customer(string _name, int _age) : base(_name, _age){
        System.Console.WriteLine("배가 고픈 "+ name +" 입니다.");
    }
    public void order(List<string> food, List<int> number, Waiter w, Chef c){
        for (int i=0; i <food.Count; i++){
            System.Console.WriteLine(name + " : "+ food[i]+" "+number[i]+ " 개 주세요!");
            pay += menu[food[i]]*(number[i]);
        }
        w.get_order(food, number);
        c.cook(food, number);
        w.serving(food, number);
    }
    public void payment(Waiter w){
        System.Console.WriteLine(name+" 손님 "+pay+"원 지불 완료");
        w.pass_on_money(pay);
    }
}

public class Employee : Person{
    public static int num_Chef = 0;
    public static int num_Waiter = 0;
    public static int salary = 50000;
    public Employee(string _name, int _age) : base(_name, _age){
    }
    public void get_salary(){
        System.Console.WriteLine(name+" 직원: "+ salary +" 원 일급받기");
    }
}

public class Chef : Employee{
    public Chef(string _name, int _age) : base(_name, _age){
        Employee.num_Chef++;
        System.Console.WriteLine("안녕하세요 "+ name +" 요리사 입니다.");
    }
    public void cook(List<string> food, List<int> number){
        for (int i=0; i <food.Count; i++){
            if(food[i] == "정식" || food[i] == "특식"){
                System.Console.WriteLine(name +" (요리담당): 서빙담당에게 주문지를 받아서 "+food[i]+" "+number[i]+ " 개 요리하기");
            }
        }
    }
}

public class Waiter : Employee{
    public static int pass_money = 0;
    public Waiter(string _name, int _age) : base(_name, _age){
        Employee.num_Waiter++;
        System.Console.WriteLine("안녕하세요 "+ name +" 웨이터 입니다.");
    }
    public void get_order(List<string> food, List<int> number){
        for (int i=0; i <food.Count; i++){
            System.Console.WriteLine(name + " (서빙담당): "+food[i]+" "+number[i]+ " 개 주문 받았습니다!");
        }
    }
    public void serving(List<string> food, List<int> number){
        for (int i=0; i <food.Count; i++){
            if(food[i] == "정식" || food[i] == "특식"){
                System.Console.WriteLine(name +" (서빙담당): "+food[i]+" "+number[i]+ " 개 요리담당에게 음식 받아서 서빙하기");
            }else{
                System.Console.WriteLine(name +" (서빙담당): "+food[i]+" "+number[i]+ " 개 서빙하기");
            }
        }
    }
    public void pass_on_money(int pay){
        pass_money += pay;
        System.Console.WriteLine(name +" (서빙담당): 손님에게서 "+ pay +"원 받기");
    }
}


class Program{
  static void Main(string[] args){
    System.Console.WriteLine("-------------- 사장님 생성 --------------");
    Owner a = new Owner("곽예진", 22);

    System.Console.WriteLine("-------------- 직원 (서빙, 요리 1명씩) 생성 --------------");
    Chef b = new Chef("나 요리잘함", 22);
    Waiter c = new Waiter("나 서빙잘함", 22);
  
    System.Console.WriteLine("-------------- 손님1 등장 --------------");
    Customer c1 = new Customer("빛이 나는 솔로", 20);
  
    System.Console.WriteLine("-------------- 손님1 정식 1개, 사이다 1개 주문 --------------");
    c1.order(new List<string>() {"정식","사이다"},new List<int>() {1,1},c,b);
  
    System.Console.WriteLine("-------------- 손님1 계산 --------------");
    c1.payment(c);
  
    System.Console.WriteLine("-------------- 손님2,3 등장 --------------");
    Customer c2 = new Customer("여보", 20);
    Customer c3 = new Customer("자기", 20);
  
    System.Console.WriteLine("-------------- 손님2,3 특식 2개, 콜라 2개 주문 --------------");
    c2.order(new List<string>() {"특식","콜라"},new List<int>() {2,2},c,b);
  
    System.Console.WriteLine("-------------- 손님2,3 계산 --------------");
    c2.payment(c);
  
    System.Console.WriteLine("-------------- 3명으로 하루 장사 마감, 사장님 종업원들에게 일급 지급 --------------");
    a.make_money();
    a.give_salary();
    b.get_salary();
    c.get_salary();

    System.Console.WriteLine("-------------- 장사를 마치고 사장이 가진 잔액 확인 --------------");
    a.check_money();
  }
}