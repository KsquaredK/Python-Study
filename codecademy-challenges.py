# ASCII Art: my initials

top_bottom_k = "K   K"
almost_top_bottom = "K  K"
almost_middle = "K K"
middle = "KK"

print(top_bottom_k + "  " + top_bottom_k)
print(almost_top_bottom + "   " + almost_top_bottom)
print(almost_middle + "    " + almost_middle)
print(middle + "     " + middle)
print(almost_middle + "    " + almost_middle)
print(almost_top_bottom + "   " + almost_top_bottom)
print(top_bottom_k + "  "  + top_bottom_k)


# Furniture Store  UPDATING VARIABLE VALUES
lovely_loveseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''

lovely_loveseat_price = 254.00

stylish_settee_description = '''Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''

stylish_settee_price = 180.50

luxurious_lamp_description = '''Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ''

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items: " + customer_one_itemization)
print("Customer One Total: " + str(customer_one_total))

#output:
#Customer One Items: Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
#Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
#Customer One Total: 333.09119999999996

# Note: line 30, use of str() to log float stored in variable to console




# Codey: Space Welterweight - ELIF
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  print("On Venus, Codey weighs " + str(weight * .91))
elif planet == 2:
  print("On Mars, Codey weighs " + str(weight * .38))
elif planet == 3:
  print("On Jupiter, Codey weighs " + str(weight * 2.34))
elif planet == 4:
  print("On Saturn, Codey weighs " + str(weight * 1.06))
elif planet == 5:
  print("On Uranus, Codey weighs " + str(weight * .92))
else:
  print("On Neptune, Codey weighs " + str(weight * 1.19))