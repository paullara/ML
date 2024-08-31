#String
name = "Paul"

print(name)

#Lists is an ordered collection of items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

#Dictionaries is collection of key-value-pairs
person = {"name": "Paul", "age": 22, "city": "San Carlos"}
print(person["name"]);
person["email"] = "paul@gmail.com"
print(person)
person.pop("age")
print(person)

#Tuples is similar to list but is immutable
point = (10, 20)
coordinates = (1.5, 2.5, 3.5);

#Summary
#Strings: Text Data, immutable.
#Lists: Ordered, mutable collection of items.
#Dictionaries: Key-value-pairs, mutable.
#Tuples: Ordered, immutable collection of items.