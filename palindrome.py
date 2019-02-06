def reverse(s):
return s[::-1]
def is palindrome(s):
#calling reverse function
rev = reverse(s)
#checking if both string are equal or not
if(s==rev):
return True
return false
# Driver Code
s="malayalam"
ans= is palindrome(s)
if ans == 1:
print("yes")
else:
print("no")
