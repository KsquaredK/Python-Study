# PYTHON PROJECTS
# 1. ASCII ART
# 2. Codey: Space Welterweight - ELIF
# 3. Magic 8-Ball
# 4. Shipping Cost Calculator


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


  # Magic 8-Ball (elif)

  import random

name = "Phineas Fogg"
question = "Is it time yet?"
answer = ""
random_number = random.randint(1,14)
# print(str(random_number))

if random_number == 1:
  answer = "Yes, definitely."
elif random_number == 2:
  answer = "It is decidely so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "The oracle is amused by your presumption, impudent one."
elif random_number == 10:
  answer = "I'm going to need more coffee."
elif random_number == 11:
  answer = "Jump on it, Jack."
elif random_number == 12:
  answer = "Dream on, dreamer."
elif random_number == 13:
  answer = "For you? But of course."
else:
  answer = "Error - out of range."

if question == "":
  print("You did not ask a question, which tears at the fabric of reality!")
elif name == "" and question != "":
  print("Question: " + str(question) + "\nMagic 8-Ball's answer is: " + answer)
else:
  print(str(name) + " asks: " + str(question) + "\nMagic 8-Ball's answer is: " + answer)



# Shipping Cost Calculator

cost = 0

#ground shipping premium
premium_ground_cost = 125

#drone shipping
drone_cost = 0

#ground shipping
if weight <= 2:
  cost = ((1.50 * weight) + 20)
elif weight <= 6 and weight > 2:
  cost = ((3 * weight) + 20)
elif weight <= 10 and weight > 6:
  cost = ((4 * weight) + 20)
else:
  cost = ((4.75 * weight) + 20)

# drone shipping calculation
if weight <= 2:
  drone_cost = (4.50 * weight)
elif weight <= 6 and weight > 2:
  drone_cost = (9 * weight)
elif weight <= 10 and weight > 6:
  drone_cost = (12 * weight)
else:
  drone_cost = (14.25 * weight)

print('Ground: ' + str(cost) + '\nPremium ground: ' + str(premium_ground_cost) + '\nDrone: ' + str(drone_cost))