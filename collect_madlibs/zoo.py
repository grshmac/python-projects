def madlib():
    n = -1
    while n<0:
        try:
            n= int(input("number: "))
        except:
            print("Please enter a no!")

    # n=None
    # while True:
    #     try:
    #         n=int(input("number: "))
    #         if n>=0:
    #             print("Enter +ve no.")
    #         else:
    #             break
    #     except ValueError:
    #         print("Please enter a no!")

    # n = None
    # while True:
    #     try:
    #         n = int(input("Enter a number: "))
    #         if n<0:
    #             break
    #     except ValueError:
    #         print("That's not a number! Try again.")

    adjective = input("adjective: ")
    animal = input("animal: ")
    verb_past_tense = input("verb to past the tense: ")
    adverb = input("adverb: ")
    adjective2 = input("adjective: ")
    noun = input("noun: ")

    madlib= f'Today I went to the zoo and saw a(n) {adjective} {animal} jumping up and down in its tree. \
          "It {verb_past_tense} {adverb} through the large tunnel that led to its {adjective2} {noun}.'

    print(madlib)
