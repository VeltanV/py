def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # Your code here
    temp = []
    for value in L:
        if not temp:
            temp.append(value)
        else:
            if(value > temp[len(temp) - 1]):
                temp.append(value)



    return temp




order = [2,4,3,5,6]
print(longest_run(order))
