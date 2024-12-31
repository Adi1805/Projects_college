#Password Generator
import string#used to used string methods
import random
s1 = string.ascii_lowercase#this is a set of string named "s1" with lowercase letters.ascii__lowercase is a method of string which has lower case letters
#print(s1)
s2 = string.ascii_uppercase#this is a set of string named "s2" with uppercase letters.ascii__uppercase is a method of string which has upper case letters
#print(s2)
s3 = string.digits#it will contain digits from o to 9.digits is a method of string.Password digits as well in most cases so we have included it
#print(s3)
s4 = string.punctuation#it contains special symbols which are used in password
#print(s4)
plen = int(input("Enter password length:"))#Asking the user to enter the length of password in integer format
s=[]#made one empty list
#Now we have used here extend method() of list in Python and not append method()
#I wil tell you why we have used extend()method and not append() method
#a=[1,2,3,4,5,6]
#b=[5,7]
#a.append(b)
#Output:-[1,2,3,4,5,6,[5,7]]
#This is the output using append method so we can see the square brackets are also coming when appended now lets see the extend method case
#a=[1,2,3,4,5,6]
#b=[5,7]
#a.extend(b)
#Output:-[1,2,3,4,5,6,5,7]
#Now here no square brackets are coming and the b list elements are appended in a so we have used extend() method instead of append method()
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#Now here we have written list before the brackets like for example
#list(s1) so here s1 is orginally a string of lowercase characters
#s1='abcdefghijklmnopqrstuvwxyz'
#now after using list(s1) the output will be
#['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#same for others
#so by using list we are converting string into list dataype
#print(s)#so now we have got the list of all the elements which we will use to make the password and it is in sorted order
#Now we will use random elements from this list to generate a password so we have used import random at the begining of the code
random.shuffle(s)#as list s is sorted order so the password may not be generated that strong.Like if we give password length of 4 so the password may contain only alphabets and no special characters.so we have shuffled the lements randomly in the list
#print(s) Now the list will not be in sorted order it would be in random order
print("Your password is:")
print("".join(s[0:plen]))# s[0:plen] means we are selecting the first plen elements from the list s.
#For example, if plen is 6, and s = ['@', 'A', 'z', '1', '$', 'b', '%'], then s[0:6] would give ['@', 'A', 'z', '1', '$', 'b'].
#join() is a string method used to combine elements of a list into a single string.
#"".join(...) means we are combining the elements of the list into a string with no separator between them.
#If the list is ['@', 'A', 'z', '1', '$', 'b'], then "".join(...) will result in the string @Az1$b.