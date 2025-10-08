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

t = int(input())

for i in range(t):
   number = int(input())
   if number == 0:
       print(0)
       continue
   while number > 0:
       print(number % 10, end=" ")
       number //= 10
   print()