## if案例
```bash
age=int(input("Enter your age: "))
if age>=18:
  print("You are eligible to vote")
elif 0<age<18:
  print(f"You are not eligible to vote. You have to wait for {18-age} years")
else:
  print("Invalid age")
print(f"You are {age} years old")
```
## if嵌套
```bash
if bool(input("Do you have a ticket? ")):
  if int(input("How long is your knife? "))<=20:
    print("You can enter the movie")
  else:
    print("You cannot enter the movie, you can't bring it")
else:
  print("You cannot enter the movie, you need a ticket")
```
## 逻辑运算符
```bash
x and y
x or y
not x
```
## 三元表达式
```bash
a=1
b=2
print(a if a>b else b)
print('a is bigger') if a>b else print('b is bigger')
```
## 数字版石头剪刀布
```bash
import random
people = int(input('请出拳：剪刀（0），石头（1），布（2）'))
computer = random.randint(0,2)
print(f'电脑的出拳是{computer}')
if people == computer:
  print('平局')
elif (people == 0 and computer == 1) or (people == 1 and computer == 0) or (people == 2 and computer == 0):
  print('电脑赢了')
elif (people == 0 and computer == 2) or (people == 1 and computer == 0) or (people == 2 and computer == 1):
  print('你赢了')
```
## 文字版石头剪刀布
```bash
import random
people = input('请出拳：')
computer = random.choice(['石头','剪刀','布'])
print(f'电脑的出拳是{computer}')
if people == computer:
  print('平局')
elif (people == "石头" and computer == "布") or (people == "剪刀" and computer == "石头") or (people == "布" and computer == "剪刀"):
  print('电脑赢了')
elif (people == "石头" and computer == "剪刀") or (people == "剪刀" and computer == "布") or (people == "布" and computer == "石头"):
  print('你赢了')
```
