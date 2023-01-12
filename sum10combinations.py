import itertools

numbers = [1, 2, 3, 7, 7, 9, 10]
# Code searcghed through nums using i in range. Then takes in listed nums and calculates all possible sums of 10, 
# if a sequence of numbers adds up to 10 the code will print these out
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 10]
print(result)
