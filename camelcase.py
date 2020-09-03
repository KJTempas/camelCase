def camel_case(sentence):
    title_case = sentence.title() #uppercase first letter of each word
    upper_camel_cased=title_case.replace(' ' ,'') #remove spaces
    #lowercase first letter, join w/ rest of string
    #slices don't produce index out of bounds errors
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence:  ')
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()