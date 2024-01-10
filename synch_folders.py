import pathlib
import os
import time
import logging
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# terminal logging
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

# terminal output and log writing
def getLogs(message, logFile):
    logging.basicConfig(level=logging.INFO, filename=logFile, filemode="a", format="%(asctime)s - %(message)s")
    logging.info(message)
    logger.info(message)


def synchAndCreate(source, replica, logFile):
    for file in pathlib.Path(source).iterdir():
        targetPath = replica+"/"+os.path.basename(file)
        if pathlib.Path.is_dir(file):
            try:
                os.mkdir(targetPath)
                getLogs("Directory "+targetPath+" created", logFile)
                print(file," ", targetPath)
                synchAndCreate(file, targetPath, logFile)
            except:
                synchAndCreate(file, targetPath, logFile)
        else:
            with open(file,"r") as sourceFile, open(replica+"/"+os.path.basename(file),"w") as targetFile:
                for line in sourceFile:
                    targetFile.write(line)
                getLogs("File at {0} copied to {1}".format(sourceFile,targetFile), logFile)


def synchAndDestroy(source, replica, logFile):
    for file in pathlib.Path(replica).iterdir():
        sourcePath = source+"/"+os.path.basename(file)
        if os.path.isdir(file):
            synchAndDestroy(sourcePath, file, logFile)
            if not os.path.isdir(sourcePath):
                os.rmdir(file)
        elif os.path.exists(sourcePath):
            continue
        else:
            os.remove(file)
            getLogs("{0} destroyed".format(file), logFile)


# Command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("sourceFolder", help="Folder to be made a backup of")
parser.add_argument("replicaFolder", help="Backup folder")
parser.add_argument("logFile", help="File to keep logs")
parser.add_argument("interval", default=30, type=int, help="Interval in minutes of backup procedure")
parser.add_argument("-S", "--seconds", default=30, type=int, help="Interval in seconds of backup procedure")
parser.add_argument("-H", "--hours", default=1, type=int, help="Interval in hours of backup procedure")
parser.add_argument("-D", "--days", default=1, type=int, help="Interval in days of backup procedure")
args = vars(parser.parse_args())

# Parameters
src = args["sourceFolder"]
replica = args["replicaFolder"]
logFile = args["logFile"]
interval = args["interval"]

if not os.path.isdir(replica):
    os.mkdir(replica)
while(True):
    synchAndCreate(src,replica,logFile)
    synchAndDestroy(src,replica,logFile)
    time.sleep(interval)
