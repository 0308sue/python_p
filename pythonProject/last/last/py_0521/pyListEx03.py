ages = [34, 56, 30, 15, 19]

adult_ages = list(filter(lambda x:x >= 19, ages))

print(adult_ages)

adult_ages2 = [x for x in ages if x>=19]
print(adult_ages2)