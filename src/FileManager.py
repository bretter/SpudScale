#!/usr/bin/python3
import csv


def readData(fileName):
    """Reads existing data file and returns contents.

    Args:
        fileName: string; name of file to read.

    Returns:
        List of lists of strings; with all data previously recorded."""
    history = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            history.append(row)
    return history


def writeData(fileName, dataToWrite):
    """Appends values in CSV format to an output file.

    Args:
        dataToWrite: list of strings; containg all data to be written to file.

    Returns:
        None
    """
    with open(fileName, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, 'excel')
        writer.writerow(dataToWrite)
