from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def isFloat(a):
    return False

if len(nums) == 1:
    print('A')
elif len(nums) == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    if nums[0] - nums[1] == 0:
        check = 1
        for i in range(n):
            if nums[0] != nums[i]:
                check = 0
        if check == 1:
            print(nums[0])
        else:
            print('B')
    else:
        a = (nums[1] - nums[2]) // (nums[0] - nums[1])
        a_r = (nums[1] - nums[2]) % (nums[0] - nums[1])
        b = nums[1] - (nums[0] * a)
        if a_r != 0:
            print('B')
        else:
            check = 1
            for i in range(len(nums) - 1):
                if nums[i + 1] != (nums[i] * a) + b:
                    check = 0
                    break
            if check == 0:
                print("B")
            else:
                num = (nums[-1] * a) + b
                print(int(num))
