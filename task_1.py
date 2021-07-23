#The height of the fence
N = int(input('Input the height of the fence:'))

#Quantity
M = int(input('Input the quantity of the fence:'))

#The height of the trees
H = int(input('Input the height of the trees:'))

result = 0
trees = 0

if  1 <= N <= H <= 100 and 1 <= M <= 100:
    while result < M:
        result += H // N
        trees += 1

else:
    print('Invalid values entered')

print(trees)