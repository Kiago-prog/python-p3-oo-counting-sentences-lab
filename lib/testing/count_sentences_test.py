#!/usr/bin/env python3

from count_sentences import MyString

import io
import sys

class TestMyString:
    '''MyString in count_sentences.py'''

    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString()
        assert(type(string) == MyString)

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        string.value = 123
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The value must be a string.\n")

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        assert(MyString("Hello World.").is_sentence() == True)
        assert(MyString("Hello World").is_sentence() == False)

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        assert(MyString("Is anybody there?").is_question() == True)
        assert(MyString("Is anybody there").is_question() == False)

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        assert(MyString("It's me!").is_exclamation() == True)
        assert(MyString("It's me").is_exclamation() == False)

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        empty_string = MyString()
        complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        assert(simple_string.count_sentences() == 3)
        assert(empty_string.count_sentences() == 0)
        assert(complex_string.count_sentences() == 4)

        
class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use setter to apply validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # Split on punctuation (., !, or ?) followed by optional whitespace
        parts = re.split(r'[.!?]', self.value)
        # Count non-empty trimmed fragments
        return len([p for p in parts if p.strip()])
