
def str(s):
    s1 = ''
    for i in range(len(s)):
        s1=s1+s[-i-1]
    return s1
s = 'Hello, world'
s1=str(s)
print(s1)
