# PYTHON PROJECTS
# 1. ASCII ART
# 2. Codey: Space Welterweight - ELIF
# 3. Magic 8-Ball
# 4. Shipping Cost Calculator
# 5. Pizza Shop


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

# output: 
# K   K  K   K
# K  K   K  K
# K K    K K
# KK     KK
# K K    K K
# K  K   K  K
# K   K  K   K


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




# Pizza Shop - modifying lists and 2D lists
# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
print("Number of $2 slices: " + str(num_two_dollar_slices) + "\n")
# output: Number of $2 slices: 3

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza! \n")
# output: We sell 7 different kinds of pizza! 

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()
print("Sorted pizzas: " + str(pizza_and_prices) + "\n")
# output: Sorted pizzas: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]


cheapest_pizza = pizza_and_prices[0]
print("Cheapest slice: " + str(cheapest_pizza) + "\n")
# output: Cheapest slice: [1, 'cheese']

priciest_pizza = pizza_and_prices.pop()
print("Priciest slice: " + str(priciest_pizza) + "\n")
# output: Priciest slice: [7, 'anchovies']

pizza_and_prices.pop()
print("Pizza and prices with anchovies gone " + str(pizza_and_prices) + "\n")
# output:Pizza and prices with anchovies gone [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage']]

pizza_and_prices.insert(-1, [2.5, "peppers"])
print("Pizzas and prices with peppers added: " + str(pizza_and_prices) + "\n")
# output: Pizzas and prices with peppers added: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage']]

three_cheapest = pizza_and_prices[0:4]
print("Three cheapest: " + str(three_cheapest))
# output: Three cheapest: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni']]



# Carly's Clippers - Lists Comprehensions and Loops
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0

for price in prices:
  total_price += price
  
print(total_price) # output: 255

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))
# output: Average Haircut Price: 31.875

new_prices = [price - 5 for price in prices]

print(new_prices)
# output: [25, 20, 35, 15, 15, 30, 45, 30]

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
# output: Total Revenue: 1085

average_daily_revenue = total_revenue / 7
print(average_daily_revenue) # output: 155.0

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]

print(cuts_under_30)
#output: ['pixie', 'crew', 'bowl']


# Physics Problems - using functions to perform calculations

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = f_temp -32 * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
# output: 82.22222222222223

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
# output: 32.0

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")
# The GE train supplies 226800 Newtons of force.

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
# output: A 1kg bomb supplies 90000000000000000 Joules.

def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " of work over " + str(train_distance) + " meters.")
# output: The GE train does 22680000 of work over 100 meters.



