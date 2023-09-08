def camelcase(sentence):
	""" Convert sentence to camelCase, for example, "Display all books"
	is converted to "displayAllBooks" """

	title_case = sentence.title() # Uppercase first letter of each word
	upper_camel_case = title_case.replace(' ', '')


	return  upper_camel_case[0:1].lower() + upper_camel_case[1:]


def main():
	sentence = input('Enter your sentence')
	output = camelcase((sentence))
	print(output)

if __name__ == '__main__':
	main()