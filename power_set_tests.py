from create_set import get_power_set

def make_set(list):
    # Converts a list of sub-lists to a set of tuples.
    return set(tuple(x) for x in list)

# 3 expected cases
print('generates the correct number of permutations', len(get_power_set([1,2,3])) == 8 )
print('contains the empty set', True if [] in get_power_set([1,2,3,4,5]) else False  )
print('generates all possible combinations of items', make_set([[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]) == make_set(get_power_set([1,2,3])) )

# 3 edge cases 
print('works with strings and numbers', len(get_power_set(['hello', 1, 'a string'])) == 8)
print('works with a single item', get_power_set([0]) == [[], [0]] )
print('works with negative numbers', len(get_power_set([-3, 1, 'hello', 4])) == 16)