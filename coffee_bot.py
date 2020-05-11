# Define your functions
def coffee_bot():
  size = get_size()
  print(size)
  drink_type = get_drink_type()
  print(drink_type)
  return "Welcome to the Cafe"

  
def print_message():
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == "a":
      return "small"
    elif res == "b":
      return "medium"
    elif res == "c":
      return "large"
    else:
      print_message()
      return get_size()  

def get_drink_type():
  res = input("What type of drink would you like ?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == "a":
    return "brewed coffee"
  elif res == "b":
    return "mocha"
  elif res == "c":
    return "latte"
  else:
    print_message()
    return get_drink_type

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2%milk \n[b] Non-fat milk \n[c] Soy milk \n")
  return res

  
# Call coffee_bot()!
coffee_bot()
