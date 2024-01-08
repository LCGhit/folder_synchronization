import pathlib
import os

sourcePath = pathlib.Path('./source/')
targetPath = './replica/'

def synch(source, replica):
    for file in source.iterdir():
        if pathlib.Path.is_dir(file):
            os.mkdir(replica+"/"+os.path.basename(file))
            synch(file, replica+"/"+os.path.basename(file))
        else:
            with open(file,'r') as source, open(replica+"/"+os.path.basename(file),'a') as targetFile:
                for line in source:
                    targetFile.write(line)
synch(sourcePath,targetPath)
