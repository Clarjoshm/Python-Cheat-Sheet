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

# 9. NUMBERS
# You are going shopping.
# Store the number of cucumbers you want to buy in a variable called cucumbers.
# The store doesn't sell partial cucumbers.
cucumbers = 2
# Next Each cucumber costs 3.25 doubloons.
price_per_cucumber = 3.25
# Then Create a new variable called total_cost
total_cost = cucumbers * price_per_cucumber
print(total_cost)

# 10. TWO TYPES OF DIVISION
# Create a variable cucumbers that holds 100 and num_people that holds 6.
cucumbers = 100
num_people = 6
# Create a variable called whole_cucumbers_per_person that is
# the integer result of dividing cucumbers by num_people.
whole_cucumbers_per_person = cucumbers/num_people
print('%.2f' % (whole_cucumbers_per_person))
# Create a variable called float_cucumbers_per_person
# that holds the float result of dividing cucumbers by num_people.
# Print float_cucumbers_per_person to the console.
float_cucumbers_per_person = whole_cucumbers_per_person

print('%.2f' % (float_cucumbers_per_person))

# SIDENOTES

# INTERGER
# Variables can also hold numeric values.
# The simplest kind of number in Python is the integer,
# which is a whole number with no decimal point
# EXAMPLE
int1 = 1
int2 = 10
int3 = -5

# FLOAT
# A number with a decimal point is called a float.
# You can define floats with numbers after the decimal
# point or by just including a decimal point at the end
# You can also use a scientific notation,
# for example e indicates the power of 10
# EXAMPLE
float1 = 1.0
float2 = 10.
float3 = -5.5e2
