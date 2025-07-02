list=[52,52,514,2,4,1,58,14,1,1,4,4,541,]
target=58

left=0
right=len(list)-1

while True:
	if left < right:
		mid=left+right//2

	if list[mid] == target:
		print(mid)

	if list[mid] < target:
		left=mid+1

	else:
		right = mid-1
print(-1)


