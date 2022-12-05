# itertools is python module of iterators
from itertools import chain, combinations


# chain iterator returns one element from each of the following iterators
# combinations iterator returns all the combinations of length r from iterable s
def powerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


st = list()
print('Enter the elements of the set: ')

# filling up the set with elements
while 1:
    el = input()
    if el == 'stop':
        break
    else:
        st.append(el)

print(list(powerSet(st)))
