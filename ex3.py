#The below line types in "I will now count my chickens"
print ("I will now count my chickens:")

#The below line counts the number of hens by adding 5 (30/6) to 25
print("Hens", 25+30/6)
#The below line counts the number of roosters and introduces the concept of the Modulus...
#...which functions like a clock/remainder function. order of operations here vital. 25*3%4 all same priorty...
#so do all at once, left to right... 25*3%4. 25*3 = 75. 75%4 = 3 (75/4 = 18 with 3 remainder!) 100-3 = 97
#at end added ("float(x)" function to make floating point numbers (with extra decimal)"
print("Roosters", float(100 - 25 * 3 % 4))

#below is text introducing what youll do in following formula
print("Now I will count the eggs:")

#below is calcuation of eggs, where division and modulus take precedent.
#4%2 = 0 (no remainder), 1/4 = 0.25. So 3+2+1-5+0-.25+6 = 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#below is another text introduction of following calculation
print("Is it true that 3 + 2 < 5 - 7?")

#below will make calculation on left and calculation on right and deliver if true or false
print(3 + 2 < 5 - 7)

#below asks a question then calculates it
print("What is 3 + 2?", 3 + 2)
print("What is 5-7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

#below deliver true/false based on calculations
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
