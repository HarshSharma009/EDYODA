n  = int(input())
# Write your code here
num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] 
i = 12
flag=True
while n!=0 and n<4000: 
	flag=False
	div = n // num[i] 
	n %= num[i] 
	while div: 
		print(sym[i], end = "") 
		div -= 1
	i -= 1
if flag:
	print(False)
