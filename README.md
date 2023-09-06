# Highlight PDF in Python

<!-- ABOUT THE PROJECT -->

## About The Project

This projects help users to highlight the keywords and export the PDF files on request.

<!-- GETTING STARTED -->

## Getting Started

To use this project, please follow the following steps.

### Prerequisites

Python is required in this project.

### Installation

Clone the repository

```
git clone https://github.com/nahceigna/highlight-pdf-python.git
```

<!-- IMPLEMENTATION -->

## Implementation

**Required arguements:**

1. -p/--file-paths: file paths

2. -k/--keywords: keywords

All the file paths and keywords have to be separated by comer ','

To run the programme:

```
python main.py -p <file paths> -k <keywords>
```

For example:

```
python main.py -p sample_pdf/sample_1.pdf,sample_pdf/sample_2.pdf -k and,text
```

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/en/latest/document.html#Document.save)
- [GitHub PyMuPDF-Utilities](https://github.com/pymupdf/PyMuPDF-Utilities/tree/master)
