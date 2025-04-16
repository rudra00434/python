list=[]
list.append(int(input("enter the 1st number: ")))
list.append(int(input("enter the 2nd number: ")))
list.append(int(input("enter the 3rd number: ")))
copy_list=list.copy()
copy_list.reverse()
if(copy_list==list):
     print("palindrome")
else:
   print("not a palindrome")
