'''
index,-index
splicing
'''
# s='Python is easy to learn'
# print(s)

# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# splicing
# s1=s[0:6]
# print(s1)
# s2=s[::2]
# print(s2)
# s3=s[::-1]
# print(s3)

'''
find the palendrome of a string,number
num=121
che=num
rev=0
while num>0:
    res=num%10
    rev=rev*10+res
    num=num//10
if rev==che:
    print(che,'is palndrome')
else:
    print(che,'is not a palndrome') 

s='wow'
rev=''       
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
if s==rev:
    print('palndrome')
else:
    print('not a palndrome') 
'''

# st='python'
# st1='pychram'

# print(st+st1)
# print(st*3)

# print(dir(str))
# formating
'''s='Python'
print(s.find('h',s.find('h')+1))
print(s.rfind('b'))
print(s.index('y'))
print(s.rindex('y'))
print(s.ljust(10,'*'))
print(s.rjust(10,'*'))
print(s.zfill(10))
print(s.center(10,'*'))'''

'''s='    Python    '
print(s.lstrip())
print(len(s.rstrip()))
print(len(s.strip()))'''

# s='python is very tuf to learn'
# print(s.replace('tuf','easy'))

# s1='python'
# s2='abc'
# print(s1.join(s2))

# print(s.split(' ',1))
# s3='''hi there!
# how are you 
# i am doing fine
# what about you
# '''
# print(s3.splitlines())

s='python is easy to learn'
print(s.startswith('python'))
print(s.endswith('n'))
print(s.removeprefix('py'))
print(s.removesuffix('rn'))


