class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m=0
        x=0
        y=2
        flag=False
        while (y<=len(num)-1):
            if num[x]==num[x+1] and num[x+1]==num[y]:
                m=max(m,int(num[x]))
                flag=True
            x+=1
            y+=1
        if flag:
            return str(m)*3
        else:
            return ""