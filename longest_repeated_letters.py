import sys


def findLongestRepeatedLetters(lines):
    # Your code here. Writes to standard out.
    count = 1
    max_list = []
    for string in lines:
        string_dict = {}
        for i in range(len(string)):
            try:
                if string[i] == string[i+1]:
                    count += 1
                else:
                    if string_dict.get(string[i]):
                        current_value = string_dict[string[i]]
                        new_value = max(count, current_value)
                        string_dict[string[i]] = new_value
                    else:
                        string_dict[string[i]] = count
                    count = 1
            except IndexError:
                if string_dict.get(string[i]):
                    current_value = string_dict[string[i]]
                    new_value = max(count, current_value)
                    string_dict[string[i]] = new_value
                else:
                    string_dict[string[i]] = count
        max_value = max(string_dict.values())
        max_keys = [(k, v) for k, v in string_dict.items() if v == max_value]
        if len(max_keys) > 1:
            max_keys.sort(key=lambda x: x[0])
        max_key = max_keys[0]
        max_list.append(max_key)
        count = 1
    for key, value in max_list:
        print(key, value)
