#Dictionary 
a = {"Bihan":99 , "Ashwin":98 ,"Arnav":54}
print(a)
print(a["Bihan"])
print(a.get("Bihan"))

a["Bihan"] = 100
print(a)

a["Suhas"] = 20
print(a)

print(len(a))

for i in a:
    print(i)

for i in a:
    print(i,"-",a.get(i))