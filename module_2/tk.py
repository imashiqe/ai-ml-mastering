# taka = 50

# if taka > 500:
#     print("I will buy a laptop")
# elif taka > 400:
#     print("I will buy a tablet")
# elif taka > 300:
#     print("I will buy a mobile")
# else:
#     print("Save money")

# for i in range(11):
#     print(i , "Hello World")

# count = 1

# while count <= 10:
#     print(count, "Hello World")
#     count = count + 1

# sum = 0
# for i in range(1,11):
#     print (i, "is processing")

#     if i % 2 == 0: 
#        continue

#     sum = sum + i
#     print(i , "is added to the sum")


# accuracy = 95

# for i in range(20):
#     accuracy += 1
#     print(accuracy)
#     if accuracy == 100:
#         print("Accuracy is 100%")
#         break

# inp = input()

# numbers = inp.split()

# x = int(numbers[0])
# y = int(numbers[1])
# z = int(numbers[2])

# 1
# minimum = x
# maximum = x

# if minimum > y:
#     minimum = y
# if minimum > z:
#     minimum = z

# if y > maximum:
#     maximum = y
# if z > maximum:
#     maximum = z

# print (minimum , maximum)

# n = int(input())

# inp = input()
# numbers = inp.split()
# positive = 0
# negative = 0
# even = 0
# odd = 0

# for i in range(n):
#     x = int(numbers[i])

#     if x > 0:
#         positive += 1
#     elif x < 0:
#         negative += 1

#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)
# print("Positive:", positive)
# print("Negative:", negative)

# t = int(input())

# for i in range(t):
#    number = int(input())
#    if number == 0:
#        print(0)
#        continue
#    while number > 0:
#        print(number % 10, end=" ")
#        number //= 10
#    print()


# x = 5

# if x > 3:
#     print("A")
# elif x > 1:
#     print("B")
# else:
#     print("C")

# i = 0
# while i< 3:
#     i += 1
#     if i == 2:
#         print("Done")


# for  i in range(2):
#     for j in range(3):
#         if j == 1:
#             break
#         print(i , j)

# for i in range(3):
#     if i == 1:
#         break
#     print(i)

# for i in range(5):
#     if i == 2:
#         break
#     print(i, end="")


# count =0
# for n in [1,2,3,4,5]:
#     if n % 2 !=0:
#         continue
#     count +=1
# print(count)


# s = 0
# for i in range(1,5):
#     if i % 2 == 0:
#         s +=   i
#     else:
#         s -= i
# print(s)

for  i in range(5,0,-1):
    if i % 2 == 0:
     continue
if i == 3:
   break
print(i, end=" ")