from wiki_extractor import WikiTableExtract

test = WikiTableExtract(url="https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh") 

imageExtractor = test.extract_all_html(table_number=0)

#print(imageExtractor)
i = 0
for image in imageExtractor:
    print()
    print(i, image)
    i += 1
    

