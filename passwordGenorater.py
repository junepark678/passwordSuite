import random, pyperclip

password = ""

symbols = []
nums = []

alphabet = []
for letter in range(97, 123):
    alphabet.append(chr(letter))

for symbol in range(33, 47):
    symbols.append(chr(symbol))

for symbol in range(58, 64):
    symbols.append(chr(symbol))

for num in range(48, 57):
    nums.append(chr(num))


for x in range(8):
    password = password + random.choice(alphabet)

for x in range(3):
    password = password + random.choice(nums)

for x in range(2):
    password = password + random.choice(symbols)

print(password)

pyperclip.copy(password)

print("the password was copied to your clipboard")

print("Quick Tip: Use a password manager")

print("These passwords are hard to memorize")
