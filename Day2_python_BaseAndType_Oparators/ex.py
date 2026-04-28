'''a=10
print(oct(a))
print(hex(a)). ## Base conversion
print(int(0o12))
print(int(0xa))'''

# Type Conversions :
'''
Converting one data type to another data type
#implesit type conversions: the programming language it self conversts one datatype to another
#explect type converstions: we are forcably converting one datatype to another datatype
'''
a=10
int()
float()
complex()
bool()
str()

print(float(a)) ## 10.0
print(complex(a)) ##10+0j
print(bool(a)) ##Ture.  0 False None ''
print(str(a)) ##'10' 'hareesh'

f=12.59
print(str(f)) ## 12.59
print(int(f))## 12
print(bool(f)) ## True
print(complex(f)) ## 12.59+oj


print(bool(''))

# print(int(10+9j)) int can not convert a complex number
# print(float(12+9j)) float cont not complex number
print(str(10+9j))
print(bool(10+9j))


# print(int('abc')) only meaning strings can be converted into a int
print(int('10'))
print(float('10'))
print(complex('10'))
print(bool('hareesh'))


'''
Non primitive data types (list,tuple,array,bytearray,set,dict)
Seq data types:
string
list
tuple
Non-seq data types:
set
dict
'''

l=[1,2,3,4,5,6] ##brackets
print(type(l))
print(l[0])
t=(1,2,3,4,5) ##paranthasis
print(t[0])
print(type(t))
s={1,2,3,4,5}
print(type(s))
d={'a':1,'b':2,'c':3}
print(d)

name='AchieversIT'
print(name[0])