"""This script uses the simplegenerator tool to determine the gender
of the user """
#imports
import os
import sys
import MySQLdb
import MySQLdb.cursors
import unicodecsv as csv
from simpleGenderComputer import SimpleGenderComputer
reload(sys)
sys.setdefaultencoding('utf-8')

#connect to database
con = MySQLdb.connect(host='152.14.88.33', user='alisse', passwd='alt-code-326',
db='StackDB', local_infile=1, use_unicode=True, charset='utf8mb4')

#get genderComputer function to find gender of user
sys.path.append(os.path.abspath('lib/genderComputer/'))

gc = SimpleGenderComputer('nameLists')

#open up gender csv file
with open('userNew.csv', 'wb') as fp:
    myFile = csv.writer(fp)
    
    
    #get names from users
    cur = con.cursor()

    print "Loading Users"
    cur.execute("select Id, DisplayName from Users")

    #WRITE TO CSV FILE 
    columns = ['Id', 'DisplayName', 'Gender']
    myFile.writerow(columns)

# #    line1= 0
    for row in cur:

        name = row[1].split(' ')
        firstName = str(name[0]).decode('utf-8', 'ignore')
        gender = (gc.simpleLookup(firstName),)
        newRow = row+gender
        myFile.writerow(newRow)


    fp.close()
print "File done"
