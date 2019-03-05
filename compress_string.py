def compress(string):
    new_string = string[0]
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            if count > 1:
                new_string += str(count)
            # This line I don't really understand
            new_string += string[i+1]
            count = 1
    if count > 1:
        new_string += str(count)
    return new_string
