a=int(input("enter"))
tem=a
reverse=0
while a!=0:
      dig=a%10
      reverse=reverse*10+dig
      a=a//10
print(reverse)
print(a)
if reverse==tem:
      print("palindrome")
else:
      print("not palindrome")