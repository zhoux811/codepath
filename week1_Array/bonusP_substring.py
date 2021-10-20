test_cases = [
    ['laboratory', 'rat'],
    ['cat', 'meow'],
    ["CATDOG", "ATDO"],
    ["CATDOG", "ATDOGE"],
    ["CATDOG", ""],
    ['12124', '124']
]


def check(long, short):  # input1 long, input2 short
    if len(short) > len(long):
        return False
    if len(short) < 1:
        return True

    for long_idx in range(len(long)):
        short_idx = 0
        while short_idx < len(short) \
                and long_idx < len(long) \
                and long[long_idx] == short[short_idx]:
            long_idx += 1
            short_idx += 1
        if short_idx == len(short):
            return True
        else:
            long_idx += 1
    return False


for pair in test_cases:
    print(check(
        pair[0],
        pair[1]
    ))
