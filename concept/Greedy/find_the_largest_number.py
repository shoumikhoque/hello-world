def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    # If the sum of digits is 0, then a number is possible only if the number of digits is 1.
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    # sum_of_digits is greater than the maximum possible sum.
    if sum_of_digits > 9 * number_of_digits:
        return [-1]

    result = [0] * number_of_digits

    # Fill from most significant digit to least significant digit!
    for i in range(number_of_digits):
        # Place 9 to make the number largest
        if sum_of_digits >= 9:
            result[i] = 9
            sum_of_digits -= 9

        # If remaining sum becomes less than 9, then fill the remaining sum
        else:
            result[i] = sum_of_digits
            sum_of_digits = 0

    return result


# Driver code to test above function
if __name__ == '__main__':

    sum_of_digits = 20
    number_of_digits = 3

    print(find_largest_number(number_of_digits, sum_of_digits))

    sum_of_digits = 100
    number_of_digits = 2

    print(find_largest_number(number_of_digits, sum_of_digits))