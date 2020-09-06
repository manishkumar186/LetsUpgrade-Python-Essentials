# Question 1: List and its default function

data = ["jack","rohan","harry","steve","warner"]

data.append("manish")
print(data)


res2 = data[0]
print(res2)

res3 =data.count("jack")
print(res3)

res4 = data.pop()
print(res4)

res5 = data.copy()
print(res5)

res5.reverse()
print(res5)

res6 = data.index("steve")
print(res6)


# Question 2: Dictionary and its default functions

dicts = {
     "name":"manish",
     "rollno":1217050,
     "college":"Acet",
     "address":"f.g.c road amritsar",
     "pincode":143001
 }

item = dicts.items()
print(item)

key = dicts.keys()
print(key)

value = dicts.values()
print(value)

dicts.update({"phone":9915802873})
print(dicts)

dicts.popitem()
print(dicts)

dicts.pop("pincode")
print(dicts)


# Question 3: set and its default function

sets1 = {10,20,30,40,50,60}
sets2 = {30,40,70,10,20,50}

unions = sets1.union(sets2)
print(unions)

intersections = sets1.intersection(sets2)
print(intersections)

diff = sets1.difference(sets2)
print(diff)

symmetric_diff = sets1.symmetric_difference(sets2)
print(symmetric_diff)

subset = sets1.issubset(sets2)
print(subset)

superset = sets1.issuperset(sets2)
print(superset)



# Question 4: Tuple and explore default method

result = (10,50,70,100,30,120)
result1 = (80,90,125)

m1 = len(result)
print(m1)

m2 = result.count(100)
print(m2)

m3 = result.index(120)
print(m3)

m4 = result[2:5]
print(m4)

m5 = result+result1
print(m5)

for i in result:
    print(i)
    

# Question 5: String and explore default methods

string = "i am learning python from LetsUpgrade"

s1 = len(string)
print(s1)

s2 = string.upper()
print(s2)

s3 = string.title()
print(s3)

s4 = string.capitalize()
print(s4)

s5 = string.find("python")
print(s5)

s6 = string.index("LetsUpgrade")
print(s6)

s7 = string[::-1]
print(s7)


















