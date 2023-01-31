even = set(range(0, 40, 2))
print(even)

squares = (4, 9, 16, 25)

print(sorted(even))

# even minus squares
# removes similar numbers in the set
print(sorted(even.difference(squares)))  # or
square_set = set(squares)   # tuple to set
print(sorted(even - square_set))

even.difference_update(square_set)  # updating after diff


# symmetric difference

print("symmetric diff")

print(sorted(even.symmetric_difference(squares)))

print(sorted(square_set.symmetric_difference(even)))
