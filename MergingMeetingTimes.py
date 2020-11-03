def merge_ranges(meetings):

    # Merge meeting ranges

    meetings.sort()
    out = [meetings[0]]

    for i,j in meetings[1:]:
        # k,l stand for the start and the end times of the previous held meeting
        k,l = out[-1]

        # now we want to know of l is smaller OR equal to j, then we will have to merge
        if i<=l:
            out[-1] = (k, max(j,l))

        else:
            out.append((i,j))


    return out

