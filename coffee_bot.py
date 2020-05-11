# Define your functions
def coffee_bot():
    return "Welcome to the Cafe"
def get_size(drink):
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    return res

# Call coffee_bot()!
print(coffee_bot())
size = get_size(1)
print(size)