primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

print(hands)
my_favourite_things = [32, 'raindrops on roses', help]
print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])
print(planets[0:3])
print(planets[3:])
print(planets[1:-1])
print(planets[-3:])
planets[3] = 'Malacandra'
print(planets)
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
len(planets)
sorted(planets)
primes = [2, 3, 5, 7]
print(sum(primes))
max(primes)
x = 12
print(x.imag)
c = 12 + 3j
print(c.imag)
print(x.bit_length())
planets.append('Pluto')
help(planets.append)
print(planets)
planets.pop()
print(planets)
planets.index('Earth')
planets.index('Pluto')
print("Earth" in planets)
print("Calbefraques" in planets)

# Tuples
t = (1, 2, 3)
t = 1, 2, 3  # equivalent to above
print(t)
x = 0.125
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
a = 1
b = 0
a, b = b, a
print(a, b)
