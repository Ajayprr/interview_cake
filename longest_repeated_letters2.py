import sys


def findLongestRepeatedLetters(lines):
    # Your code here. Writes to standard out.
    count = 1
    max_list = []
    for string in lines:
        string_dict = {}
        for i, char in enumerate(string):
            try:
                next_char = string[i+1]

                if char == next_char:
                    # char matches next char
                    count += 1
                else:
                    # Char does not match next char
                    string_dict[char] = max(count, string_dict.get(char, 0))

                    count = 1
            except IndexError:
                string_dict[char] = max(count, string_dict.get(char, 0))

        max_value = max(string_dict.values())
        max_keys = [(k, v) for k, v in string_dict.items() if v == max_value]
        if len(max_keys) > 1:
            max_keys.sort(key=lambda x: x[0])
        max_key = max_keys[0]
        max_list.append(max_key)
        count = 1
    for key, value in max_list:
        print(key, value)


# DO NOT MODIFY BELOW THIS LINE
def main():
    lines = []

    for line in sys.stdin:
        if len(line.strip()) == 0:
            continue

        line = line.rstrip()
        lines.append(line)

    findLongestRepeatedLetters(lines)


main()
