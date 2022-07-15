#Rename files with American-style dates(MM-DD-YYYY) to European-style dates(DD-MM-YYYY)

import shutil, os, re
#creating a datePattern variable regex 
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-    
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)
rename = input('Enter the file: ')
#stating a conditional statement for amerFilename in directories
for amerFilename in os.listdir('.'):
    mo = datePattern.search(rename)
    if mo == None:
        continue
    beforePart = mo.group(1) #all text before date
    monthParth = mo.group(2) #one or two digit for the month
    dayPart = mo.group(4) #one or two digit for the day
    yearPart = mo.group(6) #four digits for the year
    afterPart = mo.group(8) #all text after the date
    
euroFilename = beforePart + dayPart + '-' + monthParth + '-' + yearPart + afterPart
#getting full absolute working paths
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
#rename the file 
print(f'Renaming"{amerFilename}" to "{euroFilename}"...')
#move the renamed file into current working directory
shutil.move(amerFilename, euroFilename)