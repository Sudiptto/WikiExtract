import requests
import pandas as pd
from bs4 import BeautifulSoup
from .extract_html import extract_all_html_helper


class WikiTableExtract:
    def __init__(self, url: str):
        self.url = url
        self.soup = None
        self.tables = []
        self.headings = []

        self._fetch_page()

    def _fetch_page(self) -> None:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        page = requests.get(self.url, headers=headers).text
        self.soup = BeautifulSoup(page, "html.parser")
        self.tables = self.soup.find_all("table")

    def get_table(self, table_number: int = 0, path: str | None = None) -> pd.DataFrame:
        if table_number >= len(self.tables):
            raise IndexError(
                f"Table index {table_number} out of range. "
                f"Only {len(self.tables)} found."
            )

        table_html = str(self.tables[table_number])
        df = pd.read_html(table_html)[0]

        if path:
            df.to_html(path, index=False)
            print(f"Table {table_number} saved to {path}")

        #print(f"Table {table_number} has {len(df)} rows and {len(df.columns)} columns")

        return df
    
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