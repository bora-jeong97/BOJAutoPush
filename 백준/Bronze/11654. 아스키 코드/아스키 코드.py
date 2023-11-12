import sys
I = sys.stdin.readline
'''
ord(x) :문자를 아스키 코드로
chr(x) : 아스키 코드를 문자로
'''

n = I().rstrip()    # .rstrip() 은 공백제거
print(ord(n))
