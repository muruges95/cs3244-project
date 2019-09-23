import csv
import operator
import os
import string

def read_csv(file):
    data = ()
    with open(file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data += (tuple(row), )
    return data

#convert excel column letter to number
def col2num(col):
	num = 0
	for c in col:
		if c in string.ascii_letters:
			num = num * 26 + (ord(c.upper()) - ord('A')) + 1
	return num

def filterColumns():
    folder = input("Input the folder of files to be filtered: ")
    c = input("Input columns letters(separated by spaces, uppercase) to be shown: ")
    cols = [col2num(i) for i in c.split()]
    new_folder = "(filtered)" + folder + '/'
    os.mkdir(new_folder)
    op = ()
    for file in os.listdir(folder+'/'):
        data = read_csv(folder+'/'+file)
        for row in data:
            op += (tuple(row[i-1] for i in cols),)

        with open(new_folder+file, 'w', newline = '', encoding="utf8") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(op)
        writeFile.close()
        print(file + ' filtered')

    return 'Folder created'

filterColumns()


            
        

