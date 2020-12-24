height = 5

starts = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * starts))
    starts += 2
print((' ' * height) + '|')