s = "m"  # 1
s = ""  # 0
s = "pwwkew"  # 3
s = "bbbbb"  # 1
s = "abc"  # 3


def lengthOfLongestSubstring(s) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    st = set()
    st.add(s[0])

    slow, fast, curr_l, longest = 0, 1, 1, 1

    while fast != len(s) - 1:

        if s[slow] == s[fast]:
            slow += 1
            fast += 1

        elif s[fast] in st:
            longest = max(longest, fast - slow + 1)
            slow = fast
            fast += 1
            st = {s[slow]}

        elif s[fast] not in st:
            st.add(s[fast])
            fast += 1

    return longest


print(
    lengthOfLongestSubstring(s)
)
