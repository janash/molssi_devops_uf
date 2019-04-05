"""
string_util.py
A sample repo for the MolSSI workshop at UF

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert a string to title case.

    Parameters
    ----------
    sentence: string
        String to be converted to title case

    Returns
    ----------
    ret : string
        String converted to title case.

    Example
    ----------
    >>> title_case('ThIS iS a StrInG to BE ConVerTed.')
        'This Is A String To Be Converted.'
    """

    # Check that input is string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be type string' %(sentence))

    # Handle empty string
    if len(sentence) == 0:
        raise ValueError('Cannot apply title function to empty string.')

    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()

    return ret
