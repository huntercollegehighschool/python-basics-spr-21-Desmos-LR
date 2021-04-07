'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. Those two number will be the base and height of a triangle. 
The program will then output the area of that triangle. (Reminder: the area of a triangle can be calculated by (base * height)/2 ).

What should appear on the console when this code runs:

Enter the base: 8
Enter the height: 3
The area of the triangle is 12.0

'''
#start writing your code below
print("Hi, welcome to triangle-area finder.")
try:
  side1=int(input("Enter the value of one of the triangle's legs: "))
except ValueError:
  side1=int(input("Re-enter the value of one of the triangle's legs, this time using numerals(e.g. 0,1,2,3...): "))
try:
  side2=int(input("Enter the value of the triangle's other leg: "))
except ValueError:
  side2=int(input("Re-enter the value of the triangle's other leg, this time using numerals(e.g. 0,1,2,3...): "))
print("The area of your triangle is",side1*side2/2)
print("Hope you enjoyed triangle-area finder!")

