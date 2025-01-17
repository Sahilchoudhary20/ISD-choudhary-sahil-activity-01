""""
Description: A client program written to verify correctness of 
the activity classes.
"""
_author_ = "ACE Faculty"
_version_ = "1.1.0"
_credits_ = "Sahil Choudhary"

from genre.genre import Genre
from library_item.library_item import LibraryItem


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        valid_inputs = LibraryItem("Atomic Habit", "James Clear", Genre.NON_FICTION)
    except ValueError as e:
        print("Error - ", e)


    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    print("TITLE - ", valid_inputs.title)
    print("AUTHOR - ", valid_inputs.author)
    print("GENRE - ", valid_inputs.genre)

    

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        invalid_inputs = LibraryItem("Atomic Habit", " ", Genre.NON_FICTION)

    except ValueError as e:
        print("Error - ", e)


if __name__ == "_main_":
    main()