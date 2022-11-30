#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Person{
    protected:
        string name;
        int age;
    public:
        Person(string, int);
        /*~Person();*/ 
};

class Owner: public Person{
    private:
        static int money;
    public:
        static int revenue;
        Owner(string, int);
        void make_money();
        void give_salary();
        void check_money();
};
int Owner::money = 1000000;
int Owner::revenue = 0;

class Customer: public Person{
    private:
        static const map<string, int> menu;
    public:
        int pay = 0;
        Customer(string, int);
        void order(vector<string>, vector<int>, Waiter, Chef);
        void payment(Waiter&); 
};

const map<string,int> Customer::menu = {{"정식",5000}, {"특식",7000}, {"콜라",2000}, {"사이다",2000}};

class Employee: public Person{
    public:
        static int num_Chef;
        static int num_Waiter;
        static int salary;
        Employee(string, int);
        void get_salary();
};
int Employee::num_Chef = 0;
int Employee::num_Waiter = 0;
int Employee::salary = 50000;

class Chef: public Employee{
    public:
        Chef(string, int);
        void cook(vector<string>, vector<int>);
};

class Waiter: public Employee{
    public:
        static int pass_money;
        Waiter(string, int);
        void get_order(vector<string>, vector<int>);
        void serving(vector<string>, vector<int>);
        void pass_on_money(int);
};
int Waiter::pass_money = 0;
