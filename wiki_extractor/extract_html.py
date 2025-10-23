
def extract_all_html_helper(tables, table_number: int = 0) -> list[list[str]]:
    """
    Custom parser to extract all data from a Wikipedia table

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

        row_data = []
        #i = 0
        for cell in cells:
            #print(i, "Cell Data: ", cell)

            # find rowspan / colspan
            rowspan = cell.get("rowspan")
            colspan = cell.get("colspan")

            # Check for background color / width (for visual 'bar' cells)
            style = cell.get("style", "")
            bg_color = None
            width = None

            if "background-color" in style:
                # crude parse for color code
                for part in style.split(";"):
                    part = part.strip()
                    if part.startswith("background-color"):
                        bg_color = part.split(":")[-1].strip()
                    elif part.startswith("width"):
                        width = part.split(":")[-1].strip()

                print(f"  ➤ Detected colored cell → width={width}, color={bg_color}, rowspan={rowspan}")


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



    return rows
