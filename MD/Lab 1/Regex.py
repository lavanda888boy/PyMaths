# introducing the string and the pattern
line = input('Introduce the arbitrary string: ')
pat = input('Introduce the pattern: ')


# regex function
def matches(string, pattern):
    # check for the empty pattern and text
    if pattern == '':
        if string == '':
            return True
        else:
            return False

    # check for the universal qualifier
    if pattern == '.*':
        return True

    # variable for monitoring the end of the string and
    # the correspondence of the first characters
    # the single character case is included
    match = (string != '' and (pattern[0] == string[0] or pattern == '.'))

    # checking whether the current part of the pattern holds a '*'
    # then the recursive function is called firstly with the pattern without
    # the first two characters and then with the arbitrary string without the
    # first character (it provides double verification of correspondence)
    if len(pattern) >= 2 and pattern[1] == '*':
        return matches(string, pattern[2:]) or (match and matches(string[1:], pattern))

    # in case the pattern does not contain the '*' character
    # we continue checking the correspondence by eliminating
    # the first characters of the string and the pattern on each step
    else:
        return match and matches(string[1:], pattern[1:])


# printing the results
print(matches(line, pat))
