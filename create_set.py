def get_power_set(values):
    x = len(values)
    result = []
    for i in range(1 << x): 
        result.append([values[j] for j in range(x) if (i & (1 << j))])

    return result


def main():
    print("enter a comma-separated list of values for the set:")
    values = input()

    print(len(values))
    # if no items are entered prompt again
    while (len(values) <= 0):
        print("enter a comma-separated list of values for the set:")
        values = input()
    
    values_list = values.split(",")

    # return early for a single item
    if (len(values_list) == 1):
        print([[], values_list])
        return

    power_set = get_power_set(values_list)
    print(power_set)


if __name__ == '__main__':  
    main()