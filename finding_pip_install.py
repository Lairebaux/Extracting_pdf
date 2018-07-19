import PyPDF2
import re
from pprint import pprint
import os


def write_pdf_to_text(pdf_file, filename):
    """write pdf to text file"""
    with open(pdf_file, "rb") as read_file:
        pdfReader = PyPDF2.PdfFileReader(read_file)
        for i in range(1, pdfReader.numPages):
            page_obj = pdfReader.getPage(i)
            d = page_obj.extractText()
            condition = "a" if os.path.exists(filename) else "w"
            with open(filename, condition) as outfile:
                outfile.write(d)

def search_char_file(filename):
    """searches entire file for regex"""
    with open(filename, "r") as read_file:
        read_char = read_file.read()
        pattern = re.compile(r"(pip install \w+[-]*[-\w+]*)")
        match = pattern.findall(read_char)
    return match


def write_to_file(filename):
    with open(filename, "w") as write_file:
        sf = read_file()
        for items in sorted(sf):
            write_file.write(f"{items}\n")


def read_file(filename, old_filename):
    s = set()
    with open(filename, "r") as read_pip:
        with open(old_filename, "r") as old_read_pip:
            read_lines = read_pip.readlines()
            read_old_lines = old_read_pip.readlines()
            for i in read_lines:
                s.add(i.strip())
            for j in read_old_lines:
                s.add(j.strip())
            for m in search_char_file():
                s.add(m.strip())
    return s


