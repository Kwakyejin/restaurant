open class Person(_name: String, _age: Int){
    var name: String = _name
    var age: Int = _age
}

class Owner(_name: String, _age: Int): Person(_name, _age){
    init{
        println("안녕하세요 ${name} 사장 입니다.")
    }
    companion object{
        var revenue = 0
        var money = 1000000
    }
    fun make_money(){
        println("사장: 서빙담당에게 ${Waiter.pass_money} 원 전달받기")
        revenue += Waiter.pass_money;
    }
    fun give_salary(){
        println("사장: 일급주기")
        money -= (Employee.num_Chef + Employee.num_Waiter)*Employee.salary
    }
    fun check_money(){
        println(money + revenue) 
    }
}
class Customer(_name: String, _age: Int): Person(_name, _age){
    companion object{
        var menu: Map<String, Int> = mapOf(
        "정식" to 5000,
        "특식" to 7000,
        "콜라" to 2000,
        "사이다" to 2000)
    }
    var pay = 0
    init{
        println("배가 고픈 ${name} 입니다.")
    }
    fun order(food:List<String>, number:List<Int>, w: Waiter, c: Chef){
        for (i in food.indices) {
            println("${name}: ${food[i]} ${number[i]}개 주세요!")
            pay += ((Customer.menu.getValue(food[i])).times(number[i])).toInt()
        }
        w.get_order(food, number)
        c.cook(food, number)
        w.serving(food, number)
    }
    fun payment(w: Waiter){
        println("${name} 손님 ${pay} 원 지불 완료");
        w.pass_on_money(pay)
    }
}

open class Employee(_name: String, _age: Int): Person(_name, _age){
    companion object{
        var num_Chef = 0
        var num_Waiter = 0
        var salary = 50000
    }
    fun get_salary(){
        println("${name} 직원: ${salary} 원 일급받기");
    }
}
class Chef(_name: String, _age: Int): Employee(_name, _age){
    init{
        Employee.num_Chef++
        println("안녕하세요 ${name} 요리사 입니다.")
    }
    fun cook(food:List<String>, number:List<Int>){
        for (i in food.indices) {
            if(food[i]=="정식" || food[i]=="특식"){
                println("${name} (요리담당): 서빙담당에게 주문지를 받아서 ${food[i]} ${number[i]} 개 요리하기")
            }
        }
    }
}
class Waiter(_name: String, _age: Int): Employee(_name, _age){
    companion object{
        var pass_money = 0
    }
    init{
        Employee.num_Waiter++
        println("안녕하세요 ${name} 웨이터 입니다.")
    }
    fun get_order(food:List<String>, number:List<Int>){
        for (i in food.indices) {
             println("${name} (서빙담당): ${food[i]} ${number[i]} 개 주문 받았습니다!");
        }
    }
    fun serving(food:List<String>, number:List<Int>){
        for (i in food.indices) {
            if(food[i]=="정식" || food[i]=="특식"){
                println("${name} (서빙담당): ${food[i]} ${number[i]} 개 요리담당에게 음식 받아서 서빙하기")
            }else{
                println("${name} (서빙담당): ${food[i]} ${number[i]} 개 서빙하기")
            }
        }
    }
    fun pass_on_money(pay: Int){
        pass_money += pay
        println("${name} (서빙담당): 손님에게서 ${pay} 원 받기");
    }
}

fun main() {
    println("-------------- 사장님 생성 --------------")
    var a = Owner("곽예진", 22)

    println("-------------- 직원 (서빙, 요리 1명씩) 생성 --------------")
    var b = Chef("나 요리잘함", 22)
    var c = Waiter("나 서빙잘함", 22)

    println("-------------- 손님1 등장 --------------")
    var c1 = Customer("빛이 나는 솔로", 20)

    println("-------------- 손님1 정식 1개, 사이다 1개 주문 --------------")
    c1.order(listOf("정식","사이다"),listOf(1,1),c,b)

    println("-------------- 손님1 계산 --------------")
    c1.payment(c)

    println("-------------- 손님2,3 등장 --------------")
    var c2 = Customer("여보", 20)
    var c3 = Customer("자기", 20)

    println("-------------- 손님2,3 특식 2개, 콜라 2개 주문 --------------")
    c2.order(listOf("특식","콜라"),listOf(1,1),c,b)
    c3.order(listOf("특식","콜라"),listOf(1,1),c,b)
    
    /*c2.order(listOf("특식","콜라"),listOf(2,2),c,b)*/

    println("-------------- 손님2,3 계산 --------------")
    c2.payment(c)
    c3.payment(c)

    /*c2.payment(c)*/

    println("-------------- 3명으로 하루 장사 마감, 사장님 종업원들에게 일급 지급 --------------")
    a.make_money()
    a.give_salary()
    b.get_salary()
    c.get_salary()

    println("-------------- 장사를 마치고 사장이 가진 잔액 확인 --------------")
    a.check_money()
}
