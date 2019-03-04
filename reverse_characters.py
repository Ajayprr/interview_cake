def reverse(lst):

    left = 0
    # start at first item
    right = len(lst) - 1
    # start at last item

    while left < right:
        # until we meet in the middle, switch the left most item with the right most item
        # and switch right most item with left most item
        lst[left], lst[right] = lst[right], lst[left]
        # increment left most to move into the middle
        left += 1
        # decrement right most to move into the middle
        right -= 1

    print(lst)
