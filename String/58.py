class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #計算最後一個英文字的字母有多少是多少 
        #要先找出最後一個空白？
        #設定count 讓他去計算有多少字母
        count = 0 
        s = s.strip() #Test case 2 把前面的空格去掉
        if not s:
            return 0
        
        for char in reversed(s): #使用 reversed() 函式是為了從字串的末尾開始遍歷，這樣可以更方便地找到最後一個單字的長度。考慮以下情況：
            if char != ' ':
                count += 1
            else:
                break 
        return count 
        
        """
        使用 reversed() 函式是為了從字串的末尾開始遍歷，這樣可以更方便地找到最後一個單字的長 度。考慮以下情況：

假設有一個字串 "Hello World "，注意這個字串末尾有一個空格。如果我們從字串的開頭開始遍歷，那麼在遇到空格之後，我們將無法確定最後一個單字的長度。

使用 reversed() 函式，我們可以從字串的末尾開始遍歷，確保我們能夠正確找到最後一個單字的長度。當我們遇到第一個非空格字符時，我們開始計算長度，直到遇到空格字符為止。這樣，我們就可以確定最後一個單字的長度。

總之，使用 reversed() 函式讓我們能夠從字串的末尾開始遍歷，這有助於解決這個問題。
"""
        