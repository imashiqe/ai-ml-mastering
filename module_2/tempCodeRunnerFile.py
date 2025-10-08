inp = input()

numbers = inp.split()

x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

1
minimum = x
maximum = x

if minimum > y:
    minimum = y
if minimum > z:
    minimum = z

if y > maximum:
    maximum = y
if z > maximum:
    maximum = z

print (minimum , maximum)