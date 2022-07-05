#Rename files with American-style dates(MM-DD-YYYY) to European-style dates(DD-MM-YYYY)

import shutil, os, re
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)
rename = input('Enter the file: ')
for amerFilename in os.listdir('.'):
    mo = datePattern.search(rename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthParth = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
euroFilename = beforePart + dayPart + '-' + monthParth + '-' + yearPart + afterPart
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
print(f'Renaming"{amerFilename}" to "{euroFilename}"...')
#move the renamed file into current working directory
shutil.move(amerFilename, euroFilename)