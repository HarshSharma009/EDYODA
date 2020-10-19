input_seq = input()
# Write your code here
d={'2':list('abc'),'3':list('def'),'4':list('ghi'),'5':list('jkl'),'6':('mno'),'7':('pqrs'),'8':list('tuv'),'9':list('wxyz')}
count=0
s=input_seq[0]
res=''
for i in input_seq[1:]:
	if i==s:
		count+=1
	else:
		res+=d[s][count]
		count=0
		s=i
res+=d[s][count]
print(res)
