nums = [int(x) for x in input().split(',')]
n = nums[0]
m = nums[1]

connectList = []

for i in range(n):

	connectList.append([int(link) for link in input().split(',')])

hospital = int(input())

# for i in range(n):

    # if (i != hospital - 1) and (connectList[i][hospital-1] == 0):
	
	
connection = []

for i in range(n):
    for j in range(i):
	    connection.append(connectList[i][j])

print(connection)

	    
	    