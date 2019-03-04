def merge_meetings(meetings):
    """function takes an unsorted list of tuples and merges them into a new list of merged tuples
    tuples where the start time of the meeting is before the ending time of another meeting in the list 
    are merged into that tuple so we have fewer blocks of time where meetings are running concurrently"""

    # sort meeting list
    meetings = sorted(meetings)
    # initialize merged list using first item of sorted meetings list
    merged_meetings = [meetings[0]]
    # unpack and interate through sorted list
    for start, end in meetings:
        # get and unpack last item in the merged list so we can check if we should merge the new meeting into it
        last_merged_start, last_merged_end = meetings[-1]
        if start <= last_merged_end:
            # reassign last item in merged meeting to the new merged tuple, checking to see if the new end should be
            # the end of our current tuple, or the last end, meaning the current tuple would be totally subsumbed by the
            # old tuple
            merged_meetings[-1] = (last_merged_start,
                                   max(last_merged_end, end))
            # else, just add the current tuple
        else:
            merged_meetings.append((start, end))
