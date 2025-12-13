def convert_number_to_words(number):
    digit_words = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }

    num_str = str(number)
    return " ".join(digit_words[d] for d in num_str)
