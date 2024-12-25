#from turtle import left, right
nums = [-1, 0, 3, 5, 9, 12]
target = 3
left1 = 0
a = len(nums)
right1 = a - 1
# print("left:", left1)  # 0
# print("right:", right1)  # 5

mid = (left1 + right1) // 2


for i in range(5):
    if nums[mid] > target:
        right1 = mid + 1

    elif nums[mid] == target:
        print("mid:", mid)
    else:
        left1 = mid + 1
    mid = (left1 + right1) // 2
print("left:", left1)  # 3 # 0
print("right:", right1)  # 5 # 5
print("mid:", mid)  # 4 # 2
