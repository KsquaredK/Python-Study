# PYTHON CHALLENGES

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
# output True
print(large_power(2, 12))
# output False



def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < food_bill + electricity_bill + internet_bill + rent:
    return False
  else:
    return True

print(over_budget(100, 20, 30, 10, 40))
# output True
print(over_budget(80, 20, 30, 10, 30))
# output False



def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# output False
print(twice_as_large(11, 5))
# output True



def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20))
# output: True
print(divisible_by_ten(25))
# output: False



def in_range(num, lower, upper):
  if (num >= lower and num <= upper):
    return True
  else:
    return False

print(in_range(10, 10, 10))
# output: True
print(in_range(5, 10, 20))
# output: False



def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
# output: True
print(same_name("Tina", "Amber"))
# output: False



def always_false(num):
  if num > num:
    return True
  else:
    return False

print(always_false(0))
#  False
print(always_false(-1))
#  False
print(always_false(1))
#  False



def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating >= 5 and rating < 10:
    return "This was fun."
  else:
    return "Outstanding!"

print(movie_review(9))
# output: "Outstanding!"
print(movie_review(4))
# output: "Avoid at all costs!"
print(movie_review(6))
# output: "This one was fun."
print(movie_review(42))
# output: "Outstanding!"




def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# output: 10
print(max_num(-10, 5, -30))
# output: 5
print(max_num(-5, -10, -10))
# output: -5
print(max_num(2, 3, 3))
# output: "It's a tie!"
