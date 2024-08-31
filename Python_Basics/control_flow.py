name = input("Please Enter Your Name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Hello " + name + " You are an adult")
elif age < 18:
    print("Hello " + name + " You are a teenager")
else:
    print(name + " is dead")


names = ["Paul", "John", "Dei", "Peep"]

for name in names:
    print(name)


count = 0

while count < 3:
    print("Counting:", count)
    count += 1

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        pass
    print(i)

for i in range(3):
    print(i)
else: 
    print("Finished Loop")

countE = 0
while countE < 5:
    print("Counting with else:", countE)
    countE += 1
else:
    print("Finished loop")