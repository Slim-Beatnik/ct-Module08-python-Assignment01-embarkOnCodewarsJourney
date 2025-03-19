""" I usually use n % 2 == 0, but I found bitwise
    and thought it was clever.
    It works like this:
    4 = 0b010 -> 010
    1 = 0b001 -> 001
    so it compares these values:
    binary places:  4 2  1    4 2  1    4 2  1
                    0 1 [0] & 0 0 [1] = 0 0 [0] -> 0
    bitwise & returns bits that are both in On states,
    or literally both == 1
    so if there is no 1 in the last bit of the first
    number, the return will be 0.
    Since the last bit in off state is 0 and On is 1,
    every odd number will return 1, and even will
    return 0. It's pretty nifty.
    """
def even_or_odd(number):
    return 'Even' if (number & 1) == 0 else 'Odd'

def number_to_string(num):
    return str(num)

# apparently did this one ages ago.
def no_space(x):
    return x.replace(' ' ,'')

def get_count(sentence):
    res = 0
    for letter in sentence:
        if letter in 'aeiou':
            res += 1
    return res