import os
import argparse


def extant_file(arg):
    """Data type for -p argparse, check of the file exists
    Args:
        arg (string): input arguement for --file-paths

    Returns:
        List
    """
    paths = arg.split(',')
    for path in paths:
        if not os.path.exists(path):
            # Argparse uses the ArgumentTypeError to give a rejection message like:
            # error: argument input: x does not exist
            raise argparse.ArgumentTypeError("{0} does not exist".format(path))
    return paths


def list_of_keywords(arg):
    """Define a custom data type for -k argparse, which is a list of strings
    Args:
        arg (string): input arguement for --keywords

    Returns:
        List
    """
    return arg.split(',')
