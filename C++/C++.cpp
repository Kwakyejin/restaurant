#include "C++.hpp"
#include <string>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

/** Person **/
Person::Person(string _name, int _age) {
  name = _name;
  age = _age;
}
/** Person::~Person() { cout << "Instance removed" << endl; }**/
/*소멸자 없어도 된다고 하셔서 주석 처리 하겠습니다.*/

/** Owner **/
Owner::Owner(string _name, int _age): Person(_name, _age) {
  cout << "안녕하세요 " << name << " 사장 입니다." << endl;
}
void Owner::make_money() {
  cout << "사장: 서빙담당에게 " << Waiter::pass_money <<  " 원 전달받기" << endl;
  revenue += Waiter::pass_money;
}
void Owner::give_salary() { 
  cout << "사장: 일급주기" << endl; 
  money -= (Employee::num_Chef + Employee::num_Waiter)*Employee::salary;
}
void Owner::check_money(){
  cout << money + revenue << endl; 
}

/** Customer **/
Customer::Customer(string _name, int _age) : Person(_name, _age){
  cout << "배가 고픈 " << name << " 입니다." << endl;
}
void Customer::order(vector<string> food, vector<int> number, Waiter w, Chef c) { 
  for (int i = 0; i < food.size(); i++){
    cout << name << " : "<< food[i]<< to_string(number[i]) << " 개 주세요!" << endl;
    pay += (menu.at(food[i]))*(number[i]); 
  }
  w.get_order(food, number);
  c.cook(food, number);
  w.serving(food, number);
}
void Customer::payment(Waiter &w) { 
  cout << name <<" 손님 "<<pay <<"원 지불 완료" << endl; 
  w.pass_on_money(pay);
}

/** Employee **/
Employee::Employee(string _name, int _age) : Person(_name, _age){}
void Employee::get_salary() { 
  cout << name <<" 직원: "<< salary <<" 원 일급받기" << endl; }

/** Chef **/
Chef::Chef(string _name, int _age) : Employee(_name, _age) {
  num_Chef++;
  cout << "안녕하세요 " << name <<" 요리사 입니다." << endl;
}
void Chef::cook(vector<string> food, vector<int> number) {
  for (int i = 0; i < food.size(); i++){
    if (food[i] == "정식" || food[i] == "특식") {
      cout << name+" (요리담당): 서빙담당에게 주문지를 받아서 "+ food[i]+" "+to_string(number[i])+" 개 요리하기"<< endl;
    }
  }
  
}

/** Waiter **/
Waiter::Waiter(string _name, int _age) : Employee(_name, _age) {
  num_Waiter++;
  cout << "안녕하세요 " << _name <<" 웨이터 입니다." << endl;
}
void Waiter::get_order(vector<string> food, vector<int> number) {
  for (int i = 0; i < food.size(); i++){
    cout << name + " (서빙담당): " +food[i]+" "+to_string(number[i])+" 개 주문 받았습니다!"<< endl;; 
  }
  
}
void Waiter::serving(vector<string> food, vector<int> number) {
  for (int i = 0; i < food.size(); i++){
    if (food[i] == "정식" || food[i] == "특식") {
      cout << name+" (서빙담당): "+ food[i]+ to_string(number[i])+" 개 요리담당에게 음식 받아서 서빙하기"<< endl;
    }else{
      cout << name+" (서빙담당): "+food[i]+" "+to_string(number[i])+" 개 서빙하기"<< endl;
    }
  }
}
void Waiter::pass_on_money(int pay) {
  pass_money += pay;
  cout << name <<" (서빙담당): 손님에게서 "<< pay << "원 받기" << endl;
}


/*확인을 위한 코드*/
int main() {
  cout << "-------------- 사장님 생성 --------------"<< endl;
  Owner a("곽예진", 22);

  cout << "-------------- 직원 (서빙, 요리 1명씩) 생성 --------------"<< endl;
  Chef b("나 요리잘함", 22);
  Waiter c("나 서빙잘함", 22);
  
  cout << "-------------- 손님1 등장 --------------"<< endl;
  Customer c1("빛이 나는 솔로", 20);
  
  cout << "-------------- 손님1 정식 1개, 사이다 1개 주문 --------------"<< endl;
  c1.order({"정식","사이다"},{1,1},c,b);

  cout << "-------------- 손님1 계산 --------------"<< endl;
  c1.payment(c);

  cout << "-------------- 손님2,3 등장 --------------"<< endl;
  Customer c2("여보", 20);
  Customer c3("자기", 20);
  
  cout << "-------------- 손님2,3 특식 2개, 콜라 2개 주문 --------------"<< endl;
  c2.order({"특식","콜라"},{2,2},c,b);
  
  cout << "-------------- 손님2,3 계산 --------------"<< endl;
  c2.payment(c);

  cout << "-------------- 3명으로 하루 장사 마감, 사장님 종업원들에게 일급 지급 --------------"<< endl;
  a.make_money();
  a.give_salary();
  b.get_salary();
  c.get_salary();

  cout << "-------------- 장사를 마치고 사장이 가진 잔액 확인 --------------"<< endl;
  a.check_money();
}
  