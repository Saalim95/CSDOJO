def func(arr):
    size = len(arr)-1
    new = [0 for x in range(size+1)]
    carry = 1
    for i in range(size, -1, -1):
        res = arr[i]+carry
        if res==10:
            new[i] = 0
            carry = 1
        else:
            new[i] = res%10
            carry = 0
    if carry==1:
        print([1] + new)
    else:
        print(new)

while True:
    x = input().split()
    y =  list(map(int, x))
    func(y)
    
