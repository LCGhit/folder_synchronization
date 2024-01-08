import pathlib
import os
import time
import logging

# terminal logging
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

# output terminal log and write log file
def getLogs(message, logFile):
    logging.basicConfig(level=logging.INFO, filename=logFile, filemode="a", format="%(asctime)s - %(message)s")
    logging.info(message)
    logger.info(message)


def synchCreate(source, replica, logFile):
    source = pathlib.Path(source)
    for file in source.iterdir():
        targetPath = replica+"/"+os.path.basename(file)
        if pathlib.Path.is_dir(file):
            try:
                os.mkdir(targetPath)
                getLogs("Directory "+targetPath+" created", logFile)
                print(file," ", targetPath)
                synchCreate(file, targetPath, logFile)
            except:
                synchCreate(file, targetPath, logFile)
        else:
            with open(file,"r") as sourceFile, open(replica+"/"+os.path.basename(file),"w") as targetFile:
                for line in sourceFile:
                    targetFile.write(line)
                getLogs("File at {0} copied to {1}".format(sourceFile,targetFile), logFile)


def synchDestroy(replica, source, logFile):
    replica = pathlib.Path(replica)
    for file in replica.iterdir():
        sourcePath = source+os.path.basename(file)
        if os.path.exists(sourcePath):
            continue
        else:
            os.remove(file)
            getLogs("{0} destroyed".format(file), logFile)


while(True):
    synchCreate("./source/","./replica/","log.log")
    synchDestroy("./replica/","./source/", "log.log")
    time.sleep(15)
