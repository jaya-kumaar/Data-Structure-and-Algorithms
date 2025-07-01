nums=[5,4,6,7]
even=[]
odd=[]
output=[]
for i in nums:
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)
for i,j in enumerate(even):
	output.extend([j,odd[i]])

print(output)
