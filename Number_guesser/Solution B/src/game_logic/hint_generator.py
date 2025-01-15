def provide_hint(guess, actual_number):

    if guess <= actual_number:
        return "Try a higher number"
    else:
        return "Try a lower number"
    