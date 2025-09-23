

def extract_with_images_helper(tables, table_number: int = 0) -> list[list[str]]:
    """
    Custom parser to extract rows with images from a Wikipedia table.

    Args:
        tables (list): List of <table> elements
        table_number (int): Index of the table (0 = first)

    Returns:
        list[list[str]]: Table rows with images included
    """
    if table_number >= len(tables):
        raise IndexError(
            f"Table index {table_number} out of range. "
            f"Only {len(tables)} found."
        )

    table = tables[table_number]
    rows = []

    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        if not cells:
            continue

        has_image = False
        row_data = []

        for cell in cells:
            file_span = cell.find("span", {"typeof": "mw:File"})
            img_tag = file_span.find("img") if file_span else cell.find("img")

            if img_tag:
                has_image = True
                src = img_tag.get("srcset", img_tag.get("src", ""))
                if "," in src:
                    src = src.split(",")[-1].split()[0]
                if src.startswith("//"):
                    src = "https:" + src
                row_data.append(src)
            else:
                row_data.append(cell.get_text(strip=True))

        
        rows.append(row_data)

    #print("LENGTH OF ROWS: ", len(rows[1:]) )    
    # FIRST NON COLUMNS
    #print("LENGTH OF COLUMNS: ", len(rows[1]))

    return rows

# sample helper to check the column & row lengths:



# map images