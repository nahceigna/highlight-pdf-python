import fitz


class PdfTool:
    def __init__(self, paths, keywords):
        self.paths = paths
        self.keywords = keywords

    def take_this(self, checkword, prefix, suffix, lower):
        """Handle non-alphabetic character

        Args:
            checkword (string): check the word
            prefix (string): select, if starting like this
            suffix (string): select, if ending like this
            lower (boolean): ignore case - increases hit rate

        Returns:
            Boolean
        """
        if not prefix and not suffix:
            return True
        if lower == True:
            checkword = checkword.lower()
        if prefix and checkword.startswith(prefix):
            return True
        if suffix and checkword.endswith(suffix):
            return True
        return False

    def find_words(self, page, word_tuple, prefix="", suffix="", lower=True):
        """Make list of sub-rectangles which each contain contiguous alphabetic strings only.

        Args:
            page (fitz.fitz.Page): the number of page
            word_tuple: the word in pdf
            prefix (string): select, if starting like this
            suffix (string): select, if ending like this
            lower (boolean): ignore case - increases hit rate

        Returns:
            matches (list): list of matches
        """

        # list of matches to be returned
        matches = []
        # the word box coordinate
        rect = fitz.Rect(word_tuple[:4])

        # get page's content as a dictonary
        blocks = page.get_text("rawdict", clip=rect, flags=0)[
            "blocks"
        ]

        for block in blocks:
            for line in block["lines"]:
                if line["spans"] == []:
                    continue
                r = fitz.Rect()  # start with an empty rectangle
                checkword = ""
                for span in line["spans"]:
                    for char in span["chars"]:
                        # change the following to account for non-Latin
                        # alphabets, any exceptions, etc.
                        if char["c"].isalpha():  # alphabetic character?
                            r |= char["bbox"]  # extend current rectangle
                            checkword += char["c"]
                        else:  # non-alphabetic character detected
                            if self.take_this(checkword, prefix, suffix, lower):
                                # append what we have so far
                                matches.append((r, checkword))
                            r = fitz.Rect()  # start over with empty rect
                            checkword = ""
                if self.take_this(checkword, prefix, suffix, lower):
                    matches.append((r, checkword))  # append any dangling rect
        return matches

    def highlight_keywords(self, pdf_paths, keywords):
        """Create a new PDF file with highlighed keywords as requested.

        Args:
            pdf_path (str): The path to the PDF file.
            keywords (list): A list of keywords to highlight.

        Returns:
            None
        """
        # go through all files
        for pdf_path in pdf_paths:
            # open pdf file
            pdf = fitz.open(pdf_path)

            # go through all the pages
            for page in pdf:
                # make a list of words with its details (eg. coordinates)
                wordlist = page.get_text("words")

                # go through each words
                for word_tuple in wordlist:

                    # select the words only
                    text = word_tuple[4].lower()
                    # skip strings that are not keywords
                    if not text.startswith(keywords):
                        continue

                    # check if it is the exact keyword or not
                    matches = self.find_words(
                        page,
                        word_tuple,
                        prefix="",  # restrict to this prefix
                        suffix="",  # restrict to this suffix
                        lower=True,  # comparisons ignore upper / lower case
                    )  # get list of sub-rects and matching words

                    # go through the list of keywords
                    for match in matches:
                        # skip the empty ones
                        if match[0].is_empty:
                            continue
                        # skip what does not exactly fit
                        if not match[1].lower() in keywords:
                            continue
                        # else highlight the word`
                        annot = page.add_highlight_annot(match[0])
                        annot.update()

                # save the highlighted file
                output_file_name = pdf_path.replace(".pdf", "_highlighted.pdf")
                pdf.save(output_file_name)
