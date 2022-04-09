opening_list = ["[", "{", "("]
closing_list = ["]", "}", ")"]


def validate_brackets(string):
    stack = []

    #edge case
    if type(string) != str:
        raise Exception("Argument is not a string!")

    for i in string:
        if i in opening_list:
            stack.append(i)

        elif i in closing_list:
            if len(stack) == 0:
                return False

            if opening_list[closing_list.index(i)] == stack[len(stack) - 1]:
                stack.pop()

            else:
                return False

    return True if len(stack) == 0 else False
    


if __name__ == "__main__":
    print(validate_brackets("{bat}"))
    print(validate_brackets(""))
    print(validate_brackets("}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("(]("))
    print(validate_brackets(""))
