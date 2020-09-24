import pytest

from .string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def greet_by_name_empty():
    """Returns error if empty string."""
    expected = 'Invalid input'
    actual = greet_by_name('')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = 'onocaidicra'
    actual = reverse('arcidiacono')
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = 'ih'
    actual = reverse('hi')
    assert actual == expected

def test_reverse_empty():
    """Test reversing an empty string."""
    expected = ''
    actual = reverse('')
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = 'olleh dlrow'
    actual = reverse_words('hello world')
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = 'ih oy'
    actual = reverse_words('hi yo')
    assert actual == expected

def reverse_words_empty():
    """Test reversing words on an empty string."""
    expected = ''
    actual = reverse_words('')
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'HeLlO wOrLd'
    actual = sarcastic('hello world')
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'Hi'
    actual = sarcastic('hi')
    assert actual == expected

def test_sarcastic_empty():
    """Test sarcastic if empty string."""
    expected = ''
    actual = sarcastic('')
    assert actual == expected

def test_find_longest_empty():
    """Test find_longest with no string."""
    expected = 'Invalid input'
    actual = find_longest_word('')
    assert actual == expected

def test_return_list():
    """Test return list with one thing."""
    expected = ['apple']
    actual = return_list('apple')
    assert actual == expected

def test_return_list_empty():
    """Test return list with empty string."""
    expected = "Please supply some items"
    actual = return_list('')
    assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()
