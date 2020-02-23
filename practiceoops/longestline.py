input= open("class1.py")
longest=""
for line in input:
        if len(line) > len(longest):
            longest=line
            print("longest line=",len(longest) )
            print(longest)