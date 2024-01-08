with open('source/index.php','r') as sourceFile, open('replica/index.php','a') as targetFile:
    for line in sourceFile:
        targetFile.write(line)
