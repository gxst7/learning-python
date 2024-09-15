#Newton–Raphson method
epsilon = 0.01
k = int(input('enter a number: '))
guess = k / 2
while abs(guess**2 -k) >= epsilon:
    guess = guess - (((guess**2)  - k) / (2*guess))
print('square root of', k, 'is about', guess)