# understand
input, k = [8, 7, 9, 6, 7, 5, 1], 2  # 7
input, k = [1, 2, 3, 2, 1, 2, 3, 2, 1], 2  # 3
input, k = [1, 2, 3], 3  # null
input, k = [1, 2, 2, 1, 4, 5], 2  # 1 or 2
input, k = [], 2  # null

# match


# plan

"""
Sample Approach #1
Sort the array and find the number
* Sort the array
* Keep a counter n
* Loop through the sorted array with index a
  * If array[a] == array[a - 1], n += 1
  * Else:
    * if n == k, return array[a]
    * else, n = 0
* Return null

Time Complexity: O(n log n)
Space Complexity: O(1)
-------------------------------------------------
Sample Approach #2
Use a hash map to find number.
* Create a hash map h
* Loop through the array with index a
  * If h[array[a]] exists, h[array[a]] += 1
  * Else h[array[a]] = 1
* Loop throug hash map h with key i
  * if h[i] == k, return i
* Return null

Time Complexity: O(n)
Space Complexity: O(n)

"""

# implement

input, k = [1, 2, 2, 1, 4, 5], 2  # 1 or 2
input, k = [1, 2, 3, 2, 1, 2, 3, 2, 1], 2  # 3
input, k = [1, 2, 3], 3  # null
input, k = [], 2  # null
input, k = [8, 7, 9, 6, 7, 5, 1], 2  # 7







def sample_approach2(input, k):
    hashmap = dict()
    for e in input:
        if e not in hashmap:
            hashmap[e] = 1
        else:
            hashmap[e] = hashmap[e] + 1
    for a in hashmap:
        if hashmap[a] == k:
            print(a)

print(sample_approach2(input, k))
# review


# evaluate
