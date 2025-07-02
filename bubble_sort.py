my_arr=[52,62,4,55]

n=len(my_arr)
for i in range(n):
	for j in range(n-i-1):
		if my_arr[j]>my_arr[j+1]:
			my_arr[j],my_arr[j+1]=my_arr[j+1],my_arr[j]
print(my_arr)

