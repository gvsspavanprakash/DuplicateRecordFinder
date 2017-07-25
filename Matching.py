import xlrd
#fname of the file having data
file_location = "E:\python\SampleData.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
mylist = []
for row in range(sheet.nrows):
	mylist.append(sheet.cell_value(row,1))
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print(data[][1])
