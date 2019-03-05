def merge_sorted_lsts(lst1, lst2):
    merged_lst_size = len(lst1) + len(lst2)
    merged_lst = [None] * merged_lst_size
    current_index_lst1 = 0
    current_index_lst2 = 0
    merged_lst_index = 0
    while merged_lst_index < merged_lst_size:
        lst1_exhausted = current_index_lst1 >= len(lst1)
        lst2_exhausted = current_index_lst2 >= len(lst2)
        if (not lst1_exhausted and (lst2_exhausted or lst1[current_index_lst1] < lst2[current_index_lst2])):
            merged_lst[merged_lst_index] = lst1[current_index_lst1]
            current_index_lst1 += 1
        else:
            merged_lst[merged_lst_index] = lst2[current_index_lst2]
            current_index_lst2 += 1
        merged_lst_index += 1
    print(merged_lst)


merge_sorted_lsts([1, 3, 5], [2, 4, 6])
