import pandas as pd


excel_sheet = pd.read_excel(r'/Users/tanayamoghe/Desktop/hair.xlsx', sheet_name=None, header=None)
excel_sheet = excel_sheet['Brandwise Attributes']

end_row = int(input("Enter number of brands: "))

dict = {}
for i in range(3, end_row+3):
        dict[excel_sheet.at[i, 0]] = excel_sheet.at[i, 7]

print(dict)

dict_2 = {}
for i in range(3, end_row+3):
#gives the dictionary of prices by top brands
        dict_2[excel_sheet.at[i, 0]] = excel_sheet.at[i, 4]

print(dict_2)

dict_3 = {}
for i in range(3, end_row+3):
#gives the dictionary of MRP by top brands
        dict_3[excel_sheet.at[i, 0]] = excel_sheet.at[i, 5]

print(dict_3)

dict_4 = {}
for i in range(3, end_row+3):
#gives the dictionary of Avg discount by top brands
        dict_4[excel_sheet.at[i, 0]] = excel_sheet.at[i, 6]

print(dict_4)












