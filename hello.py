# print("Hello world")

# print(20+40)

# print()

# slice

# n1="how are youy"

# print (n1[:4])
# print (n1[4:])

# print ("firt 4 chrator:",n1[:4],"Remaing chartor:",n1[4:]);


# b ="Hello, world"

# print (b[-5:-2])

# c = " Happy Diwali!   "
# print(c.upper())
# print(c.lower())
# print(c.strip()) # returns "Hello, World!"
# print(c.replace("l", "K"))
# print(c.split())

# text = "hello world"
# print(text.capitalize())

# name = "Rahul"
# age = 20
# txt = (f"My name is {name} and I am {age} years old.")
# print(txt)

# word =["i","love","birds"]

# print(" ".join(word))

# def myFrutes(f):
#     print(f"i like Frutes {f}")

# frutes =["Apple","Banana","orange","Grape","Gava"]

# for frute in frutes:
#     print(frute)
#     if frute == "orange" :
#         myFrutes(frute)

def myshop():
 fruit =""   
 shop = 3

 match shop :
    case 1 :
        fruit = "Orange"
    case 2:
        #print("Banana")
         fruit = "Banana"
    case 3:
        #print("Grapes")
        fruit = "Grapes"
    case 4:
        #print("Gava")
        fruit = "Gava"
    case _:
        #print("Not Found")
        fruit = "Not Found"
 return fruit

print(myshop())


# 30 days  in month
# 1 first gold rate 20000
# 2 21000

# har din 1k increment in gold rate
# total end of 30 th day

# def Calculategold(day,total):
#     gold_percentage =(day/total)*100
#     return gold_percentage
    
#     gold_rate =20000
#     day =1
#     total =30
#     gold_percentage =Calculategold(day,total)
#     print(f"golad percentage: {gold_percentage}%")



# while day <=1 :
#     print(f"Day{day}:{gold_rate}")

#     total=total+gold_rate
#     gold_rate = gold_rate+1000
#     day = day+1
#     print(f"total number days:{total}")


def calculate_gold(day, total):
    gold_percentage = (day / total) * 100
    return gold_percentage


gold_rate = 20000
total = 30

percentage = 5

while percentage <= 100:
    day = (percentage / 100) * total
    print(f"{percentage}% = Day {day}")
    percentage += 5