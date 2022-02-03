from typing import List
from dagster import job, op
import os
import mdfreader


def files():
    file_dir = []
    entries = os.listdir('C:/UserData/f97668/Messungen/')
    for entry in entries:
        if entry.endswith(".dat"):
            file_dir.append(os.path.join('C:/UserData/f97668/Messungen/', entry))
    return file_dir


def mdf_files(files: List):
    mdf_obj = []
    for file in files:
        print(mdf_obj.append(mdfreader.MdfInfo(file)))


def dateien():
    mdf_files(files())

dateien()