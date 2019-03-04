def reverse_words(message):
    reverse_characters(message, 0, len(message)-1)
    current_word_start_index = 0

    for i in range(len(message) + 1):

        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):

    while left_index < right_index:

        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1
