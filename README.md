# Highlight PDF in Python

<!-- ABOUT THE PROJECT -->

## About The Project

This projects help users to highlight the keywords and export the PDF files on request.

<!-- GETTING STARTED -->

## Getting Started

To use this project, please follow the following instructions.

1. Clone the GitHub repository

   Begin by cloning this repository using this command:

   ```
   git clone https://github.com/nahceigna/highlight-pdf-python.git
   ```

2. Set up the Python environment, replace environment name `highligh_pdf_env` if necessary

   ```
   conda create -n highligh_pdf_env python=3.9 -y
   conda activate highligh_pdf_env
   ```

3. Install dependencies by navigating to the `highlight-pdf-python` directory and install the required dependancy as follow:

   ```
   cd highlight-pdf-python
   pip3 install -r requirements.txt
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
