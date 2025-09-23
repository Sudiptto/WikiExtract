from wiki_extractor import WikiTableExtract

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India"
    extractor = WikiTableExtract(url)

    # Get DataFrame and also save it as HTML
    # df = extractor.get_table(table_number=1, path="tests/tableHTML/debug_table.html")
    # print(df.head())

    # Get custom parsed rows (with images only)
    
    rowTableLength = extractor.extract_with_image_length(table_number=1) 
    tableLength = extractor.get_Table_length(table_number=1)
    
    print("tableLength: ", tableLength)
    print("tableLength: ", rowTableLength)
    

