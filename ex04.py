#--coding:utf-8--
#汽车数
cars = 100
#一辆汽车内的空间
space_in_a_car = 4.0
#司机数目
drivers = 30
#乘客数目
passengers = 90
#不被开的车的数量
cars_not_driven = cars - drivers
#被开的车的数量
cars_driven = drivers
#合伙用车的容纳量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车几个乘客
average_passengers_per_car = passengers / cars_driven


#在字符串中穿插已定义的变量，需要以   “字符串1”，变量，“字符串2”  的形式

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Study Drills 
#错误原因：car_pool—capacity 在之前没有定义，，应该是 carpool-capacity 才对
#1题  其实我感觉没有太大必要啊...最多也只会使后面的120.0变成 120
#2题  浮点数就是有小数点的数
#3题  注解如上
#4题  =为变量命名  

