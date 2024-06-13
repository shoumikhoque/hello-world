def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of Arrival Timing
    :param departure: A list of Departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    result = 0
    count = 0
    n = len(arrival)

    for index in range(n):
        count = 0
        for i in range(1, n):
            if arrival[index] <= arrival[i] <= departure[index]:
                count += 1

        if result < count:
            result = count

    return result


# Driver code to test above function
if __name__ == '__main__':
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))