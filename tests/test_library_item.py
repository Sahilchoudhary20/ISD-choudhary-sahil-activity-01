"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
_author_ = "Sahil Choudhary"
_version_ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    
    def test_init_valid_inputs_attributes_set(self):
        expected = LibraryItem("Atomic Habit", "James Clear", Genre.NON_FICTION)

        self.assertEqual("Atomic Habit", expected._LibraryItem__title)
        self.assertEqual("James Clear", expected._LibraryItem__author)
        self.assertEqual(Genre.NON_FICTION, expected._LibraryItem__genre)

    def test_init_title_blank_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(" ", "James Clear", Genre.NON_FICTION)

    def test_init_author_blank_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("Atomic Habit", " ", Genre.NON_FICTION)

    def test_init_invalid_genre_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("Atomic Habit", "James Clear", "NON_FICTION")

    def test_title_accessor_returns_title(self):
        expected = LibraryItem("Atomic Habit", "James Clear", Genre.NON_FICTION)
        self.assertEqual("Atomic Habit", expected.title)

    def test_author_accessor_returns_author(self):
        expected = LibraryItem("Atomic Habit", "James Clear", Genre.NON_FICTION)
        self.assertEqual("James Clear", expected.author)

    def test_genre_accessor_returns_genre(self):
        expected = LibraryItem("Atomic Habit", "James Clear", Genre.NON_FICTION)
        self.assertEqual(Genre.NON_FICTION, expected.genre)
