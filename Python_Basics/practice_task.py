# ----------------------Add two numbers---------------------------------
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = (a + b)
print("addition of two num is = ", c)

#--------------------------- Find the square root-----------------------
print ("exponent:", a**2)
print ("Square root of = ", b**2)

# -------------------------Find area of traingle------------------------
Area_Traingle = (a*b)/2
print ("Area of trangle is = " ,Area_Traingle)

#------------------------ Swap two variables----------------------------
print("a value is = " ,a)
print("b value is = " ,b)
temp = a
a = b
b = temp
print('The value of a after swapping a: {}'.format(a))
print('The value of b after swapping b: {}'.format(b))

# ---------------------Convert Kilometers to miles----------------------
kilometers = float(input("Enter the kilometers: "))
print (kilometers)
                        # Conversion
conversion_factor = 0.621
miles = kilometers*conversion_factor
print ('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# Miles to kilometers
miles = float(input("Enter the miles: "))
print ("Miles is = ", miles)
conversion_factor = 0.621
kilometers = miles/conversion_factor
print("Kilometers is =", kilometers)


#----------------------- Convert celsius to fahrenheit---------------------

celsius = float(input("Enter the number celsius degree: "))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

#--------- Check if number is positive negative or zero----------------------
number = float(input("Enter any number: "))
if number > 0:
   print("this is Positive number  ")
elif number == 0:
   print("this is Zero number  ")
else:
   print("this is Negative number  ")

#----------------- check number is odd or even-------------- ---------------
number = int(input("Enter the number which is odd or even: "))
if (number % 2) == 0:
   print("{0} is Even".format(number))
else:
   print("{0} is Odd".format(number))

#-------------------------------Leap year----------------------------------
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


#------------- Find largest number among three numbers----------------------
x = int(input("Enter x vaule : "))
y = int(input("Enter y value : "))
z = int(input("Enter z value : "))
if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z
print("The largest number is = ", largest)