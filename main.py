def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books"
    is converted to "displayAllBooks" """

    title_case = sentence.title()  # Uppercase first letter of each word
    upper_camel_case = title_case.replace(' ', '')  # remove spaces
    # Lowercase first letter, join 	with rest of string
    # Slices don't produce index out of bounds errors.
    # So this still works on empty strings, strings of length 1
    return upper_camel_case[0:1].lower() + upper_camel_case[1:]


def main():
    banner()
    sentence = input('Enter your sentence')
    output = camelcase(sentence)
    print(output)


def banner():
    print('Camelcase Program')


if __name__ == '__main__':
    main()
