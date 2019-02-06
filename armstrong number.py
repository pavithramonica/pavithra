num = 1634
# change num variables to string,
# and calculated the length(number of digits)
order=len(str(num))
#initialize sum
sum 0
#find the sum of the cube of each didgit
temp=num
while temp>0:
digit=temp%10
sum+=digit**order
temp//=10
# display the result
if num==sum:
print (num,"is an armstrong number")
else:
print(num,"is not an armstrong number")
