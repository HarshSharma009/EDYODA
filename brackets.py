brackets  = input()
# Write your code here
d={'(':')','{':'}','[':']'}
l=[]
flag=True
for i in brackets:
	if i in '{([':
		l.append(d[i])
	elif l!=[] and l[-1]==i:
		l.pop()
	else:
		flag=False
		break
print(flag)
