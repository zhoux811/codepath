# Understand
'''
Input: nums1 = [1, 2, 3, 4], nums2 = [2, 3, 4]
Output: [2, 3, 4] (any order)
'''

# Match:
'''
- hashmap
	- key -> element, value -> count
	- decrement the count
	- {9: 1}
- iterate through the largest list

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

nums1 = [4, 4, 4]
nums2 = []


def intersect(nums1, nums2):
    largest_lst = nums2
    smaller_lst = nums1
    if len(nums1) > len(nums2):
        largest_lst = nums1
        smaller_lst = nums2

    hmap = {}
    for elem in largest_lst:
        if elem in hmap:
            hmap[elem] += 1
        elif elem not in hmap:
            hmap[elem] = 1

    output = []
    for elem in smaller_lst:
        if elem in hmap and hmap[elem] != 0:
            hmap[elem] -= 1
            output.append(elem)

    return output


print(intersect(nums1, nums2))

'''
Time: O(N)
Space: O(N)

Notes:
- write out and test edge cases
	- 1 or 2 (more important)
- match, plan, steps are intermingled
- try to recognize different patterns before 	 implementing with brute force
- Plan step: carefully clarify algorithm (decrementing step for outputting)
	- most important: code takes 4-5 min, algorithm step most important
	- are you getting stuck in the midde implementation (such a range for interview gives hints)
		- hints not bad, unless giving hint. Rather perfect ability not get a hinkt OR to take and run with the hint
- run through urself. catch mistakes.
- have no good plan: brute force.
- ask specific time and space (sometimes care, if they specifically said)
	- if you have different approaches clarify with the interviewer to double check
'''
