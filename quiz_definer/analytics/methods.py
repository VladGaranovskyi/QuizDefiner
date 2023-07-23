

def insertion_sort(dict_df):
    count = len(dict_df["count"])
    if count <= 1:
        return
    for i in range(1, count):

        key = dict_df["count"][i]
        key2 = dict_df["result"][i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key > dict_df["count"][j]:
            dict_df["count"][j + 1] = dict_df["count"][j]
            dict_df["result"][j + 1] = dict_df["result"][j]
            j -= 1
        dict_df["count"][j + 1] = key
        dict_df["result"][j + 1] = key2
