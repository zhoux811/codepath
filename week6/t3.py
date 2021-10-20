from collections import Counter


s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "a"

# Output: "BANC"


# Output: "a"

def minWindow(s: str, t: str) -> str:
    Ls, Lt = len(s), len(t)

    if Ls < Lt:
        return

    l, r = 0, Lt - 1  ###

    ans = "", 0, Ls - 1

    t_dict = Counter(t)

    while l <= Ls - Lt and r <= Ls - 1:
        print('\ncurrent window %s' % s[l:r + 1])
        for k in t_dict:
            if k in s[l:r + 1] and t_dict[k] <= Counter(s[l:r + 1])[k]:
                print('\t%s letter is ok' % k)
                pass
            else:
                print('\t%s letter is not ok, r +=1' % k)
                r += 1
                l -= 1
                break
            if k == t[-1]:
                if r - l < ans[2] - ans[1]:
                    print('\t\treaggesting ans\'s l r  %s ( %d  %d ) to %s ( %d %d )\n\t\ttry l -=1' % (
                    s[ans[1]: ans[2]+1], ans[1], ans[2], s[l:r+1], l, r))
                    ans = s[l:r + 1], l, r
                else:
                    print('\t\tsubstring good. but not better/shorter than %s ' %s[ans[1]: ans[2]+1])
        l += 1

    return ans[0]


print(minWindow(s, t))
