print("Welcome to the love calulator")
name = input("What is your full name?")
caste = input("What is their name?")

both_names = name + caste
lower_names = both_names.lower()
l = lower_names.count("l")
a = lower_names.count("a")
h = lower_names.count("h")
i = lower_names.count("i")
first_digit = l + a + h + i

s = lower_names.count("s")
y = lower_names.count("y")
m = lower_names.count("m")
n = lower_names.count("n")
second_digit = s + y + m + n

score = int(str(first_digit) + str(second_digit))

if (score > 50):
  print(f"Your score is {score},you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
