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
        self.valid = False

        try: 
            self._fetch_page()
            self._load_dataframe()
            self._set_heading()

            self.valid = True

        except Exception as e:
            print(f"❌ Initialization failed: {e}")

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

        if not self.tables:
            raise ValueError("No tables found on page.")


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
        self.data_frame = pd.read_html(table_html, flavor="bs4")[0]
        
    def _set_heading(self):
        """Extract multi-level headings as a list of lists (matrix form)."""
        if self.data_frame is None:
            raise ValueError("DataFrame not loaded yet. Call _load_dataframe() first.")

        columns = self.data_frame.columns

        # If it's a MultiIndex (multi level heading), we have multiple header rows 
        if isinstance(columns, pd.MultiIndex):
            levels = len(columns[0])
            headings = []

            # Initialize empty lists for each header row
            for _ in range(levels):
                headings.append([])

            #  populate each level
            for col_tuple in columns:
                for i in range(levels):
                    headings[i].append(col_tuple[i])
        else:
            # Single-level header
            headings = [list(columns)]

        # after construction of headings 

        # algo: go backwards, if any TWO values are DIRECTLY the same, than pop (headings can only have valid columns ...)

        i = -1
        while headings and i >= len(headings) * -1:
            row = headings[i]
            valid = True

            for j in range(1, len(row)):
                if row[j] == row[j-1]:
                    #print(row[j], row[j-1])
                    valid = False
                    break  

            if valid == False:
                headings.pop(i)

            i -= 1

        self.headings = headings

    # heading is going to take
    def get_heading(self):
        # check if db has been parsed alr
        return self.headings
    

    # get dataframes
    def get_data_frames(self):
        return self.data_frame
        

    def extract_all_html(self) -> list[list[str]]:
        """
        Extract rows that contain images, using helper function.
        """
        return extract_all_html_helper(self.tables, self.table_number) 
    
    