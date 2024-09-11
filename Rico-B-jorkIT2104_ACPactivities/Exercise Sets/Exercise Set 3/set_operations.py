set1 = {8,16,24,32,44}
set2 = {7,14,8,32,21}

difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print(f"Set 1 - Set 2 = {difference_set1}")
print(f"Set 2 - Set 1 = {difference_set2}")

union_set = set1.union(set2)
print(f"Set 1 Union Set 2 = {union_set}")

symdiff_set1 = set1.symmetric_difference(set2)
symdiff_set2 = set2.symmetric_difference(set1)

print(f"The symmetric difference of set 1 to set 2 is {symdiff_set1}")
print(f"The symmetric difference of set 2 to set 1 is {symdiff_set2}")

intersection_set1 = set1.intersection(set2)
intersection_set2 = set2.intersection(set1)

print(f"The intersection of set 1 to set 2 is {intersection_set1}")
print(f"The intersection of set 2 to set 1 is {intersection_set2}")