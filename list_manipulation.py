# list_manipulation
# Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).

# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list


def list_manipulation(l, command, location, value=None):
    if command == 'remove' and location == 'end':
        return l.pop()
    elif command == 'remove' and location == 'beginning':
        return l.pop(0)
    elif command == 'add' and location == 'beginning':
        l.insert(0, value)
        return l
    elif command == 'add' and location == 'end':
        l.append(value)
        return l