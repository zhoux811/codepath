sample = "G"
sample = "ABC"
sample = ""
sample = "333222111"
sample = "3"
sample = 'aabbaa'
sample = "wwwwaaadexxxxxaaax"

ans2 = ""

if  len(sample) == 0:
    print( None )
else:
    ans2 += sample[0]

counter = 1
temp_c = sample[0]
for c in sample[1:]:
    if c == temp_c:
        counter += 1
    else:
        ans2 += str(counter)
        ans2 += c
        temp_c = c
        counter = 1
ans2 += str(counter)

print(ans2)