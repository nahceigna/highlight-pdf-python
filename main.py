"""
@created: 20-07-2023
@author: Nahceigna

This code searches and highlights the keywords for PDF files.

Documentations:
    * https://pymupdf.readthedocs.io/en/latest/document.html#Document.save
    * https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/word%26line-marking/mark-words.py

TODO: a more organised way to store keywords

"""

# import required library
import argparse
from ctypes.wintypes import PDWORD
from pdf_tools import PdfTool
import arg_types as TYPE

if __name__ == "__main__":
    # initialise parser
    description = "Upload file path and enter keywords for highlighing PDFs, separated by comer \',\'"
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Adding arguement
    parser.add_argument("-p", "--file-paths", dest="paths_in_list",
                        type=TYPE.extant_file, help="file path")
    parser.add_argument("-k", "--keywords", dest="keywords_in_list",
                        type=TYPE.list_of_keywords, help="keywords in lowercase")

    args = parser.parse_args()

    # create highlight objects
    files = PdfTool(tuple(args.paths_in_list), tuple(args.keywords_in_list))
    # highlight words and output pdf file
    files.highlight_keywords(files.paths, files.keywords)
