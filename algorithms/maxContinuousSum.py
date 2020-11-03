l = [-2,2,5,-11,6]
d = [1,1,1,-1,10]

# we want to implement the Kadane's algorithm here

# h1 Let's start with a brute-force solution at first
# For the intuitive version, we will want to first
# generate all the possible subarrays and then find
# the max and return it


def bruteforce(arg):

    '''
    This is an intuitive brute force approach with O(n^2) complexity
    ARGS: input 1d list
    OUT: the maximum possible, and the subarray that has gives that sum
    '''
    # create a list for all arrays to append here
    arrays = []

    # iterate over the input array
    for element in range(len(arg)):
        # generate all possible subarrays
        for following_elements in range(element+1, len(arg)):
            arrays.append(arg[element : following_elements])

    # find each some for each subarray if you only need the sum
    sums = map(lambda x: sum(x), arrays)
    max_sum = max(sums)

    # if you need the actual array
    # then iterate over the arrays and save them

    max_sum = sum(arrays[0])
    max_sum_idx = 0

    for _ in range(len(arrays[1:])):
        if sum(arrays[_]) > max_sum:
            max_sum = sum(arrays[_])
            max_sum_idx = _

    # return the highest sum and the subarray
    return max_sum, arrays[max_sum_idx]



def kadanealgo(arg):
    '''
    This is a more advanced algorithm that returns the highest sum
        and runs in O(n) time
    ARGS: input 1d list
    OUT: max sum, and the subarray that gives it
    '''

    # set current and max sums to element 0
    current_sum = arg[0]
    max_sum = current_sum

    # now, for every element in the array
    # check if adding it to a current sum increases the current sum
    # or if it's better to start a new sum either way
    for element in arg[1:]:
        current_sum = max(element, current_sum + element)
        max_sum = max(current_sum, max_sum)
    # at this point max sum is already the desired sum


    ############################################################################


    # now let's implement the same algorithm, but keep track of the subarray too


    current_sum = arg[0]
    max_sum = current_sum

    start_idx, end_idx, tmp_idx = 0,0,0


    for idx in range(1,len(arg)):

        # if element by itself is already bigger than the sum
        # tham start the whole current sum over
        if arg[idx] > current_sum + arg[idx]:
            current_sum = arg[idx]
            tmp_idx = idx

        # else, just add it to the current sum
        else:
            current_sum += arg[idx]

        # in case the current sum is greater that the current max
        # then get the tmp_idx (the point where we started this
        # current sum). And the index of the iteration: the point
        # where we are currently at.
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx = tmp_idx
            end_idx  = idx

    print(arg[start_idx : end_idx + 1])

    return max_sum


print(kadanealgo(d))

























