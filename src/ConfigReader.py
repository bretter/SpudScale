import os
import yaml


def configReader():
    fileName = 'spudscale.config'
    dirName = os.path.dirname(os.path.abspath(__file__))
    pkgdDirName = dirName.replace('library.zip', '')
    config = {}

    try:
        stream = open(fileName, 'r')
    except FileNotFoundError:
        try:
            pkgdFile = pkgdDirName + fileName
            stream = open(pkgdFile, 'r')
        except FileNotFoundError:
            raise
    for data in yaml.load_all(stream):
        config = data
    config['scales'] = scaleIndexToAddress(config['scales'])
    return config


def scaleIndexToAddress(scaleIndexedNames):
    scaleAddressNames = {}
    for index, name in scaleIndexedNames.items():
        scaleAddressNames[chr(ord('A') + (index - 1))] = name
    return scaleAddressNames
