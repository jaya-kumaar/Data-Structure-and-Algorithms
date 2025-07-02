def linearSearch(stack,target):
    if target in stack:
        return True
    else:
        return False

def linearsearch(stack,target):
    for i in stack:
        if i == target:
            return stack.index(i)







stack=[1,2,4,5,6,7]
target=4

print(linearSearch(stack,target))
print(linearsearch (stack,target))