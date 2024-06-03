def trace_path(path):
    dictionary = dict(path)
    reverse_dict = dict()
    # To fill reverse_dict, iterate through the given dict
    keys = dictionary.keys()
    for key in keys:
        reverse_dict[dictionary.get(key)] = key
    # Find the starting point of itinerary
    start = None
    for key in keys:
        if key not in reverse_dict:
            start = key
            break
    result = []
    # Trace complete path
    dest = dictionary.get(start)
    while dest is not None:
        result.append([start, dest])
        start = dest
        dest = dictionary.get(dest)
    return result




if __name__ == '__main__':
    paths = [
        # [["NewYork", "Chicago"], ["Boston", "Texas"], ["Missouri", "NewYork"], ["Texas", "Missouri"]],
        # [["Sydney", "Dubai"], ["LosAngeles", "Cairo"], ["Paris", "Rome"], ["Cairo", "Paris"], ["Rome", "Tokyo"],
        #  ["Tokyo", "Sydney"]],
        # [["Vienna", "Athens"], ["London", "Berlin"], ["Madrid", "Rome"], ["Paris", "Vienna"], ["Rome", "Paris"],
        #  ["Athens", "Moscow"], ["Berlin", "Madrid"]],
        # [["Singapore", "Sydney"]],
        [["HongKong", "Taipei"], ["Osaka", "Seoul"], ["Taipei", "Singapore"], ["Tokyo", "Osaka"],
         ["Beijing", "Shanghai"], ["Seoul", "Beijing"], ["Singapore", "KualaLumpur"], ["Shanghai", "HongKong"]]
    ]

    for i, path in enumerate(paths):
        print("{}. \tInput: {}".format(i + 1, path))
        print("\tOutput: {}".format(trace_path(path)))
        print("-" * 100)