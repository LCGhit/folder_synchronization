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


# adds whatever new files/folders to backup folder
def synchAndCreate(source, replica, logFile):
    for file in pathlib.Path(source).iterdir():
        targetPath = replica+"/"+os.path.basename(file)
        # recursiveness for folders
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


# deletes whatever new files/folders to backup folder
def synchAndDestroy(source, replica, logFile):
    for file in pathlib.Path(replica).iterdir():
        sourcePath = source+"/"+os.path.basename(file)
        # recursiveness for folders
        if os.path.isdir(file):
            synchAndDestroy(sourcePath, file, logFile)
            # source folder may be empty but still exist
            if not os.path.isdir(sourcePath):
                os.rmdir(file)
                getLogs("{0} destroyed".format(file), logFile)
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
parser.add_argument("interval", type=int, help="Interval in seconds for backup procedure")
parser.add_argument("-u", "--unit", choices=["m", "h", "d"], help="Turns interval argument into different unit")
args = vars(parser.parse_args())

# set interval unit according to unit argument
def intervalUnit(argument):
    match argument:
        case("m"):
            intervalInSecs = args["interval"]*60
            return intervalInSecs
        case("h"):
            intervalInSecs = args["interval"]*3600
            return intervalInSecs
        case("d"):
            intervalInSecs = args["interval"]*3600*24
            return intervalInSecs
        case(_):
            intervalInSecs = args["interval"]
            return intervalInSecs

# Parameters
src = args["sourceFolder"]
replica = args["replicaFolder"]
logFile = args["logFile"]
interval = intervalUnit(args["unit"])


# script put into action
if not os.path.isdir(replica):
    os.mkdir(replica)

if not os.path.exists(logFile):
    with open(logFile, "w"): pass

while(True):
    synchAndCreate(src,replica,logFile)
    synchAndDestroy(src,replica,logFile)
    time.sleep(interval)
