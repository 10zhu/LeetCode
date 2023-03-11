class Solution:
    def decodeString(self, s: str) -> str:
        def findBracket(lst):
            start=-1
            final=-1
            for i in range(0,len(lst)):
                if lst[i]=="[":
                    start=i
                if lst[i]=="]":
                    final=i
                    break
            if(start!=-1 and final!=-1):
                # lst.pop(start)
                # lst.pop(final)
                return start,final
            else:
                return -1,-1
        def findNum(lst,n):
            s=n
            for i in range(n,-1,-1):
                # print("i: ",i)
                if(lst[i].isdigit()==True):
                    s=i
                else:
                    break
            return s,n


        res=""
        lst=[]
        for i in range(0,len(s)):
            # if(s[i]!="["and s[i]!="]"):
            lst.append(s[i])
        before,after=findBracket(lst)
        # print("ba: ",before,after)
        while(before!=-1 and after!=-1):
            string=""
            check=""
            startNum,endNum=findNum(lst,before-1)
            # print("se: ",startNum,endNum)
            if(startNum!=endNum):
                for i in range(startNum,endNum+1):
                    check+=lst[i]
                    # print("c: ",check,lst[i])
            else:
                check+=lst[before-1]
            temp=int(check)
            # if(startNum!=endNum):
            #     for i in range(0,endNum-startNum):
            #         lst.pop(startNum)
            # print("t: ",temp)
            for i in range(before+1,after):
                string+=lst[i]    
            string=temp*string
            lst[before-1]=string
            
            
            # print("ba: ",before,after)
            # print("lst: ",lst)
            for i in range(0,after-before+1):
                lst.pop(before)
            # print(lst)

            if(startNum!=endNum):
                for i in range(0,endNum-startNum):
                    lst.pop(startNum)
            before,after=findBracket(lst)
            
        for i in range(0,len(lst)):
            res+=lst[i]
        return res

        