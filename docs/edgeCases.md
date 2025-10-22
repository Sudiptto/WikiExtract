#1) No column headings 

![alt text](images/image.png) 

Souce: https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India (table 0)

For this case return the JSON row values only:

{
    row1,
    row2,
}

#2) Table w/ colored rows
Source: ![alt text](images/coloredRows.png) 

https://en.wikipedia.org/wiki/List_of_governors_of_New_York (Table 0)

Try to pre-parse & populate the table w/ images straight up, delete the solid color lines 

#3) Table w/ Fragmented Rows (IE some rows are row spans)
Source: ![alt text](images/fragments.png) 

https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Bangladesh (Table 1)

#4) Several images in one table:
Source: 
https://en.wikipedia.org/wiki/List_of_sultans_of_the_Ottoman_Empire 

#5) 
![alt text](image.png)

Notes:
- Wikipedia MP cannot properly parse out the images, import wikipedia

#6) ![alt text](images/image.png)

Notes:
- Issue single column may not have the same length could be issues in column 

#7) 
![alt text](images/headingMisCalculation.png)

How it looks like on the web: ![alt text](images/bangladeshHeadingPage.png)
Notes:
- In this case the pandas libary isn't properly attending to what the correct heading is, it has 3 different headings but there could really only be one consice heading. The edge case here is that the last heading (third row) is just REPEATED, ie it's BOLDED, provisional government of bangladesh also counted as a heading.