import os

lin = 'https://vimeo.com/showcase/'

n = 9031111
for ltd in range(40):
    print(r'start ' + lin + str(n))
    os.system(r'start ' + lin + str(n))
    n -=1