def extract_all_html_helper(tables, table_number: int = 0) -> list[list[str]]:
    """
    Custom parser to extract all data from a Wikipedia table, including
    background color bars (e.g., <td style="background-color:#00BFFF;">).

    - If a <td> has a background color but no text/image, inserts the color code.
    - Keeps original behavior for images and text.
    - Prints detected color + rowspan for debugging.
    """

    if table_number >= len(tables):
        raise IndexError(
            f"Table index {table_number} out of range. Only {len(tables)} found."
        )

    table = tables[table_number]
    rows = []

    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        if not cells:
            continue

        row_data = []
        i = 0

        for cell in cells:
            # Default content (text or image)
            file_span = cell.find("span", {"typeof": "mw:File"})
            img_tag = file_span.find("img") if file_span else cell.find("img")

            if img_tag:
                src = img_tag.get("srcset", img_tag.get("src", ""))
                if "," in src:
                    src = src.split(",")[-1].split()[0]
                if src.startswith("//"):
                    src = "https:" + src
                content = src
            else:
                content = cell.get_text(strip=True)

            # Check for solid-color bar (background-color)
            style = cell.get("style", "")
            if "background-color" in style:
                for part in style.split(";"):
                    if "background-color" in part:
                        color_value = part.split(":")[-1].strip()
                        if color_value:
                            content = color_value  # replace cell with color
                            #print(
                            #    f"[{i}] Found color cell → {color_value}, rowspan={cell.get('rowspan', '')}"
                            #)
                            break

            # Append plain content (keep empty as "")
            row_data.append(content)
            i += 1

        rows.append(row_data)

    return rows
