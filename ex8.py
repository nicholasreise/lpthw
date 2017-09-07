#create a formatter variable with four format functions to print the scripts below
formatter = "{} {} {} {}"

#use formatter function to turn
print(formatter.format(1, 2, 3, 4))
#print a string with one two three four
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#print a string with the text used in the definition of the formatter variable and format function
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
