string = input()
# Write your code here
s=''
if not string[0].isupper():
	s+='Sentence must start with a Uppercase character (e.g. Noun/ I/ We/ He etc.)\n'
if len(string.split())<2:
	s+='There must be spaces between words.\n'
if string[-1]!='.':
	s+='Sentence must end with a full-stop.\n'
if '  ' in string:
	s+='Continuous spaces are not allowed.\n'
for i in range(len(string)-1):
	if string[i].isupper()and string[i+1].isupper():
		s+='Continuous uppercase characters are not allowed.\n'
		break
if string[-1].isupper() or string[-2].isupper():
	s+='However the sentence can end after an uppercase character.'
print('False\n'+s) if s!='' else print(True)
