from wiki_extractor import WikiTableExtract

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh"
    extractor = WikiTableExtract(url)

    # Get DataFrame and also save it as HTML
    # df = extractor.get_table(table_number=1, path="tests/tableHTML/debug_table.html")
    # print(df.head())

    # Get custom parsed rows (with images only)
    
    rowTableLength = extractor.extract_with_image_length(table_number=0) 

    # get table length
    tableLength = extractor.get_Table_length(table_number=0)

    df = extractor.get_table(table_number=0, path="tests/tableHTML/banglaPM.html")
    imageExtractor = extractor.extract_with_images(table_number=0)

    #print(imageExtractor)
    i = 0
    for image in imageExtractor:
        print()
        print(i, image)
        i += 1
    

    # ACCIDENTLY ACCOUNTING THE THREE DIFFERNET HEADINGS.. (BANGLADEHS HAS TWO HEADINGS SO ITS OFF BY 2 , NEED TO FIND WHERE THERE ISNT THE DIP)
    print("tableLength: ", tableLength)

    print("tableLength: ", rowTableLength)
    

