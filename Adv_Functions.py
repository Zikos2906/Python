numbers1 = [1,2,3]
numbers2 = [4,5,6]

res = map(lambda x,y:x+y,numbers1,numbers2)
print("addition of both list: ")
print( list(res))


num = [50,60,70,80,90,100]

def sq(n):
    return n*n

result = map(sq,num)
print("The Square of the number are")
print(list(result))