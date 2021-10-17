from __future__ import print_function # Python 2/3 compatibility
from datetime import date
import boto3

list1 = []
fName = ""
lName = ""
todayDate = ''


s3 = boto3.resource('s3')

dynamodb = boto3.client('dynamodb')





print("Welcome to the Movie Menu, Banner downloaded:")
s3.Bucket('4bucket123').download_file('f1/cinema.jpg', 'banner.jpg')

# Question 1 asks user if they want to see the Date, user must use Y or N
print("\nWould you like to see Todays Date? Y or N")
todayDate = input()
today = str(date.today())
while not (todayDate == 'Y' or todayDate == 'N'):
    print("Please Enter Y or N")
    todayDate = input()
if todayDate == 'Y':
    print("Today Date:", today)
elif todayDate == 'N':
    print("Date will not appear")


#First Name and validates the input
print("\nPlease Enter Your First Name:")
fName = input()
while not (fName.isalpha() == True):
    print("Please Enter Characters only")
    fName = input()
fName = str(fName)
print("First Name:", fName)

#Last Name and validates the input
print("\nLast Name:")
lName = input()
while not (lName.isalpha() == True):
    print("Please Enter Characters only")
    lName = input()
lName = str(lName)
print("Last Name:", lName)

#Age and validates the input
print("\nAge:")
age = input()
while not (age.isdigit() == True):
    print("Please Enter an Integer")
    age = input()
age = int(age)
print("Age:", age)

#Adds to 2 Movies to the List
list1.append("Coming 2 America")
list1.append("Without Remorse")

#Asks user which movie do they want to see
print("\nWhich Movie would you like to see: Coming 2 America or Without Remorse")
movieS = input()
while not (movieS in list1):
    print("Incorrect Movies please type the 2 movies avilable")
    movieS = input()
    
#Adds inputs into the Dynamodb Table 
dynamodb.put_item(TableName='Movies', Item={'MovieName':{'S':movieS},'Date':{'S': today}, 'Age':{'N': str(age)}, 'FirstName':{'S': fName}, 'LastName':{'S': lName}})

#Program Ends
print("\nYou have been added to our records, goodbye!")