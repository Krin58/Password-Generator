import random
from string import ascii_letters, digits, punctuation

a=int(input("Enter the No. of alphabets in the password:"))  # initializing size of string ascii letters that the password should contain irrespective of case
n=int(input("Enter the No. of digits in the password:"))  # initializing size of string of digits that the password should contain
_a=int(input("Enter the No. of Special Characters in the password:")) # initializing size of string of special characters that the password should contain
passwd="" # creation of an empty string to append the character

for j in range(a):
    passwd+=''.join(random.choices(string.ascii_letters)) 
for k in range(n):
    passwd+=''.join(random.choices(string.digits)) 
for s in range(_a):
    passwd+=''.join(random.choices(string.punctuation+' ')) 


passwd1=list(passwd)
random.shuffle(passwd1)
l=''.join(passwd1)
print("***\t",l,"\t***")
