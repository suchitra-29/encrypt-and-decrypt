def encryption(s,k):
  s1=" "
  for i in s:
    x=ord(i)+k
    s1+=chr(x)
  print(s1)
def decryption(s,k):
  s1=" "
  for i in s:
    x=ord(i)-k
    s1+=chr(x)
  print(s1)
s=input()
k=int(input())
op=input()
if op=="Encrypt":
  encryption(s,k)
elif op=="Decrypt":
  decryption(s,k)
else:
  print("incorrect operation")