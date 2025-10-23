import requests
import pandas as pd
from bs4 import BeautifulSoup
from .extract_html import extract_all_html_helper

# one wiki-table 
class WikiTableExtract:
    def __init__(self, url: str, table_number: int = 0):
        self.url = url
        self.soup = None
        self.tables = []
        self.headings = []
        self.data_frame = None
        self.table_number = table_number

        self._fetch_page()

    def _fetch_page(self):
        """Fetch the HTML of the page and find all <table> elements."""
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()

        self.soup = BeautifulSoup(response.text, "html.parser")
        self.tables = self.soup.find_all("table")


    def _load_dataframe(self):
        """Load the specified table into a pandas DataFrame."""
        if not self.tables:
            raise ValueError("No tables found on this page.")

        if self.table_number >= len(self.tables):
            raise IndexError(
                f"Table index {self.table_number} out of range. "
                f"Only {len(self.tables)} table(s) found."
            )

        table_html = str(self.tables[self.table_number])
        self.data_frame = pd.read_html(table_html)[0]


    # heading is going to take
    def get_heading(self, table_number: int = 0):
        # check if db has been parsed alr
        if not self.data_frame:
            table_html = str(self.tables[table_number])
            self.data_frame = df = pd.read_html(table_html)[0]


        pass
    
    def get_Table_length(self, table_number: int = 0) -> int:
        df = self.get_table(table_number, path=None)
        rows, cols = df.shape
        return [rows, cols]

        

    def extract_all_html(self, table_number: int = 0) -> list[list[str]]:
        """
        Extract rows that contain images, using helper function.
        """
        return extract_all_html_helper(self.tables, table_number) 
    
    
    def extract_with_image_length(self, table_number: int = 0) -> list:
        rows = extract_all_html_helper(self.tables, table_number) 
        return [len(rows[1:]), len(rows[1])]