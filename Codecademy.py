# Using a PRINT statement,
# output a message of your choosing to the terminal.
print("Im learning python")

# Print something using Python 3's SYNTAX.
print("I'm learning python")
print("Its going well.....")

# Try adding your name to the PRINT STATEMENT with
# the + operator so that this Python program prints "Hello [your_name]"
print("Hello "+"Josh, ")

# 4. HANDLING ERRORS
# We've written two print statements that will raise errors.
# One has mismatched quotes and the other has no quotes at all.
print("How do you make a hot dog stand?")
print("You take away its chair!")

# 5. VARIABLES
# Create a variable called todays_date and assign
# a value that will represent today's date to that variable.
todays_date = 30-12-2018
print(todays_date)

# 6. ARITHMETIC
# Multiply two numbers together and assign the result
# to a variable called product
product = 500 + 250
print(product)
# What is the remainder when 1398 is divided by 11?
# Save the results in a variable called remainder.
remainder = 1398 % 11
print(remainder)

# 7. UPDATING VARIABLES
# We're trying to figure out how much it rained
# in the past year! Update the annual_rainfall variable to
# include the values from September to December.
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

# Amount of rainfall each month
july_rainfall = 1.05
august_rainfall = 4.91
september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

# Calculation of final rainfall
annual_rainfall += august_rainfall
annual_rainfall += july_rainfall
annual_rainfall += september_rainfall + october_rainfall
annual_rainfall += november_rainfall + december_rainfall

print(annual_rainfall)

# 8. COMMENTS
# Add a comment above the declaration of city_pop
# with a description of what you think the variable contains.
city_name = "St. Potatosburg"
# This shows the population of St. Potatosburg
city_pop = 340000
