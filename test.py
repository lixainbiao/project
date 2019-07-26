import os

dir = 'D:/'
for i in os.walk(dir):
    print(i[0])
