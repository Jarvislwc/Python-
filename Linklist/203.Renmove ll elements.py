'''
 while head != None and head.val == val :
            head = head.next 
        if head == None : # 錯誤條件 
            return 
        prev = head # p 給 h 
        current = head.next # 把 h.n 丟給 c 
        while current: 
            if current.val == val: # 判斷如果c的值 == 他給的值 
                prev.next = current.next # 跳過c.v 因為一樣
                current = current.next # 拉 p
                #hi.append(current.val)   
            else :
                prev = current # c 丟給 p
                current = current.next # c 往下走
        return head # 跑出[5,6]
'''
