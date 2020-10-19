n = int(input())
# Write your code here
d,l={},[]
for i in range(n):
	s=input().split()
	d[s[0]]=s[1:]
	for j in d[s[0]]:
		if j not in l:
			l.append(j)
ans={}
for i in l:
	ans[i]=[]
	for j in d:
		if i in d[j]:
			ans[i].append(j)
print(ans)
