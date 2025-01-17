""""
Description: A class to manage LibraryItem objects.
"""
_author_ = "Sahil Choudhary"
_version_ = "1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    LibraryItem class: Used to maintain Library's data.

    """
    def __init__(self, title: str, author: str, genre: Genre):
        """
        To initialize the class attributes with attribute values.

        Args:
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The Genre of the library item.

        Returns:
            None

        Raises:
            ValueError: When title is blank, the author is blank or the genre is blank.
        
        """
        if len(title.strip()) > 0:
            self.__title = title

        else:
            raise ValueError("Title cannot be blank.")
        
        if len(author.strip()) > 0:
            self.__author = author

        else:
            raise ValueError("Author cannot be blank.")
        
        if isinstance(genre, Genre):
            self.__genre = genre
        
        else:
            raise ValueError("Invalid Genre.")
        
    @property
    def title(self) -> str:
        """
        Accessor for the title attribute.
            
        """
        return self.__title
        
    @property
    def author(self) -> str:
        """
        Accessor for author attribute.
            
        """
        return self.__author
        
    @property
    def genre(self) -> Genre:
        """
        Accessor for genre attribute.

        """
        return self.__genre


    

