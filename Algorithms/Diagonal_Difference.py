
def diagonalDifference(arr):
    r_sum=0
    l_sum=0
    for i in range(len(arr)):
      l_sum=l_sum+arr[i][i]
      r_sum=r_sum+arr[i][(len(arr)-1)-i]
    
    return abs(l_sum - r_sum)
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
