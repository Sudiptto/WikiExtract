from wiki_extractor import WikiTableExtract

test = WikiTableExtract(url="http://127.0.0.1:5500/tests/tableHTML/banglaPrimeMinister.html", table_number=0) 


'''#print(imageExtractor)
i = 0
for image in imageExtractor:
    print()
    print(i, image)
    i += 1'''
    

'''x = test.get_heading()

for i in range(len(x)):
    print(i, x[i])
    print()
'''
y = test.get_heading()
print(y[0])

z = test.get_data_frames()
headingLevels = z.columns.nlevels

print("HEADING LEVELS: ", headingLevels)
#print(z)
print()
x = test.extract_all_html()
'''for i in range(len(x)):
    print(i, x[i])
    print()'''

# matix & dataframe
def construct_matrix(m, df, heads):
    full_matrix = []
    maxSize = len(heads)

    for i in range(df.shape[0]):
        row = df.iloc[i]
        unique_values = set(row)
        if len(unique_values) == 1:
            full_matrix.append(list(row))
    

    return full_matrix

print(construct_matrix(x,z,y))