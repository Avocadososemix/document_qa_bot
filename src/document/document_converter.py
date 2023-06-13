import os
import pdfplumber
from utils import utils

def check_if_file_already_converted(file_name):
    print(utils.get_file_path(utils.file_name_without_extension(file_name) + '.txt'))
    print(utils.check_if_file_exists(utils.get_file_path(utils.file_name_without_extension(file_name) + '.txt')))
    # print(utils.check_if_file_exists("f:\Deep Learning\projects\flan-5\src\data\DnD_BasicRules_2018.txt"))
    if utils.check_if_file_exists(utils.get_file_path(utils.file_name_without_extension(file_name) + '.txt')):
        return True

def convert_file_from_pdf_to_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_into_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)