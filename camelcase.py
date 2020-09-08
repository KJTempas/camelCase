#git practice creating branches, merging; functions are separate branches
def camel_case(sentence):
    title_case = sentence.title() #uppercase first letter of each word - claraj version
    upper_camel_cased=title_case.replace(' ' ,'') #remove spaces - claraj version
    #lowercase first letter, join w/ rest of string
    #slices don't produce index out of bounds errors

    #first word in lower case and remaindert (index 1 to end) are title case
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    #display welcome banner
    message = "CAMELCASE PROGRAM"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')

def instructions():
    print('Enter a sentence to convert to camelCase')

def main():
    banner() 
    instructions()
    sentence = input('Enter your sentence:  ')
    output = camel_case(sentence)
    print(f' Your sentence in camel case looks like this {output}')

if __name__ == '__main__':
    main()