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

sum = 0
for i in range(1,11):
    print (i, "is processing")

    if i % 2 == 0: 
       continue

    sum = sum + i
    print(i , "is added to the sum")
