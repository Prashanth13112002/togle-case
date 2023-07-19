class solution:
    def toggle(self,string):
        S=""
        for i in range (len(string)):
            ascii=ord(string[i])
            if ascii >=65 and ascii <=95:
                j=ascii+32
                S+=chr(j)
            if ascii >=97and ascii <122:
                j=ascii-32
                S+=chr(j)
        return S
a1=solution()
print(a1.toggle(input()))