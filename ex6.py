#defining variable of types of people
types_of_people = 10
#setting variable that we will use later, containing types of people variable
x = f"There are {types_of_people} types of people."

#defining value for the later string
binary = "binary"
do_not = "don't"
#defining y variable, and string with function that will reference other values
y = f"Those who know {binary} and those who {do_not}."

#getting sentences moving that will be filled
print(x)
print(y)

#making it so we dont need to repeat
print(f"I said: {x}")
print(f"I also said: '{y}'")

#setting variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
