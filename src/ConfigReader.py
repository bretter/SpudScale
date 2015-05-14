import os
import yaml


def configReader():
    """Opens and extracts config options from spudscale.config.

    Returns:
        List; containing all config information."""
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
    """Replaces numerical indices with corresponding alphabetic keys.

    Args:
        scaleIndexedNames: dict; with numerical keys.

    Returns:
        Dict; with adjusted keys."""
    scaleAddressNames = {}
    for index, name in scaleIndexedNames.items():
        scaleAddressNames[chr(ord('A') + (index - 1))] = name
    return scaleAddressNames
