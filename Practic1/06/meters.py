meters = float(input("Enter distance in meters: "))

inches = meters * 39.3701   
feet = meters * 3.28084       
miles = meters * 0.000621371  
yards = meters * 1.09361     

print("Distance in inches: {:.2f}".format(inches))
print("Distance in feet: {:.2f}".format(feet))
print("Distance in miles: {:.6f}".format(miles))
print("Distance in yards: {:.2f}".format(yards))