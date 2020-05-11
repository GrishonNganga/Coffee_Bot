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
  res = input("What type of drink would you like? [a] Brewed Coffee [b] Mocha [c] Latte ")
  return res
      

    # Call coffee_bot()!
print(coffee_bot())
size = get_size()
print(size)