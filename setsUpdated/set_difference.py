from primes_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(f'Evens: {evens}')
print(f'Odds: {odds}')

primes = set(primes_generator(100))
print(f'Primes: {primes}')
squares = set(squares_generator(100))
print(f'Squares:{squares}')

# checks whats not in the comparing set
print(odds.difference(primes))
print(primes.difference(odds))
print(odds - primes)
