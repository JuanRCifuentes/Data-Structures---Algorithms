import time

nemo = ["nemo"]
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
array_1000 = ['nemo' for i in range(1000)]
array_1000000 = ['nemo' for i in range(1000000)]

def findNemo(array):
    start = time.time()*1000
    for i in array:
        if i == 'nemo':
            print('Found Nemo!')
    end = time.time()*1000
    print(f'Call to find Nemo took {end - start} miliseconds')

# findNemo(nemo)
# findNemo(everyone)
# findNemo(array_1000)
# findNemo(array_1000000)

def print1Name(names):
    start = time.time()*1000
    print(names[0]) # Always prints just the first name
    end = time.time()*1000
    print(f'Call to find Nemo took {end - start} miliseconds')

# print1Name(nemo)
# print1Name(everyone)
# print1Name(array_1000)
print1Name(array_1000000)