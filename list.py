list1 = ['a', 'b']
list1.append('c')  # 新增元素到陣列中
# print(list1)

list2 = []
list2.extend([list1[0], list1[2]])  # 把list1的元素（可同時）加入陣列中
# print(list2)

li = ['1', '2', '3', '4', '5', '6']

del li[2]  # 刪除li[2] = 3 這個元素
li.pop()  # pop最後一個元素
li.remove('4')  # 刪除指定的數值（裡面只能放陣列有的元素）
print(li)
