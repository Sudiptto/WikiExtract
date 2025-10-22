"""
Integration testing to check if pandas rows & column output matches with beautiful soup column extraction
"""
import pytest 
import pandas as pd

# TEMPORARILY ADD TO TEST
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from wiki_extractor import WikiTableExtract 

TEST_CASES = [
    ("https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India", 1),
    ("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States", 1),
    ("https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh", 0),
    # NOTE DEBUG THIS SPECIFIC CASE HERE
    ("https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh", 1)

]


@pytest.mark.integration
@pytest.mark.parametrize("url, table_number", TEST_CASES)
def test_table_shape_matches(url, table_number):
    extractor = WikiTableExtract(url)


    row_table_length = extractor.extract_with_image_length(table_number)
    table_length = extractor.get_Table_length(table_number)


    print("tableLength:", table_length)
    print("rowTableLength:", row_table_length)

    # Test if the number of rows with images matches the total number of rows
    assert row_table_length[0] == table_length[0], (
        f"Mismatch for {url}, table {table_number}: "
        f"extract_with_image_length rows ({row_table_length[0]}) != "
        f"get_table_length rows ({table_length[0]})"
    )