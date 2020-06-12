from binary_search_tree import BSTNode
import time

start_time = time.time()
# Adjusted file path to match my comp setup
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = [for if name_2.contains(name in names_1) ] 

## against the rules but runs at:
## runtime: 0.003635883331298828 seconds
# duplicates = set(names_1) & set(names_2)
# Return the list of duplicates in this data structure

duplicates = []

# Replace the nested for loops below with your improvements
# O(n²)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 in name_2:
#             duplicates.append(name_1)
# O(n)

# runtime: 1.169 seconds
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

#### Compares in unicode
### O(log n)
## runtime: 0.14600515365600586 seconds
# make the first node
list_one = BSTNode(names_1[0])
# build it out
for name in names_1:
    list_one.insert(name)
# check to see if tree contains the name, then append to duplicate
for name in names_2:
    if list_one.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
