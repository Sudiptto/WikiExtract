from wiki_extractor import WikiTableExtract

if __name__ == "__main__":
    # test with bangladesh URL
    # 
    # https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India
    # https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh
    # url = 
    url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India"
    extractor = WikiTableExtract(url)


    #df = extractor.get_table(table_number=1, path="tests/tableHTML/indiaPandas.html")


    imageExtractor = extractor.extract_all_html(table_number=1)

    #print(imageExtractor)
    i = 0
    for image in imageExtractor:
        print()
        print(i, image)
        i += 1
    

    

