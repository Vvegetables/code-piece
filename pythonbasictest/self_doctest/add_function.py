#coding=utf-8

'''
#doctest:+NORMALIZE_WHITESPACE
# doctest: +ELLIPSIS [...]
'''



def my_function(a, b):
    """
    >>> my_function(2, 3)
    5
    >>> my_function('a', '3')
    'a3'
    """

    return a + b



def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

    >>> grouped = group_by_length([ 'python', 'module', 'of', 'the', 'week' ])
    >>> grouped == { 2:set(['of']),
    ...              3:set(['the']),
    ...              4:set(['week']),
    ...              6:set(['python', 'module']),
    ...              }
    True

    """
    d = {}
    for word in words:
        s = d.setdefault(len(word), set())
        s.add(word)
    return d

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
