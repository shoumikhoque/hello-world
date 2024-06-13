import math

def egyptian_fraction(lob, hor):
    """
    Finds the egyptian fraction denominators
    :param lob: Numerator of the fraction
    :param hor: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """

    # A List to store denominator
    lst_denominator = []

    # While loop runs until fraction becomes 0 i.e,
    # numerator becomes 0
    while lob != 0:
        # taking ceiling
        x = math.ceil(hor / lob)

        # storing value in lst_denominator list
        lst_denominator.append(x)

        # updating new numerator and denominator
        lob = x * lob - hor
        hor = hor * x

    return lst_denominator


# Driver code to test above function
if __name__ == '__main__':

    print(egyptian_fraction(6, 14))
    print(egyptian_fraction(2, 3))
