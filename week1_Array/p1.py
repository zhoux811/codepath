# Understand:
# input = string
# output = string

# s = ",./"
# new_s = "/.,"

# s = "hello world!"
# new_s = "!dlrow olleh"


# Match:


# Plan:
# Traversing string
# Get the length of the string
# Create a new list
# Append characters to the list starting from the last index of the string

# for letter in string:
#   get index of last letter

# Implement:


def reverse(s):
    l = []
    for i in range(len(s), 0, -1):
        l.append(s[i - 1])

    return ''.join(l)

    # Review:

    # s = "hello"
    # index = 4
    # l =['o', 'l', 'l', 'e', 'h']

    # s = "a, b"
    # index = 0
    # l =['b', ' ', ',', 'a']

    # Evaluate:

    # Time complexity: O(N), where n is the length of the string


reverse("String")

print(reverse("String"))

