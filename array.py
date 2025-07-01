num=[1,3,2,4] 
for i in range(len(num)):
	for j in range (len(num)-i-1):
		if num[j]%2 != 0:
			num[j],num[j+1]=num[j+1],num[j]
print(num)

