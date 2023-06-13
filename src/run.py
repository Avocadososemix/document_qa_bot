import argparse

from document import document_converter
from utils import utils, logger

logger = logger.getLogger()

doc = 'DnD_BasicRules_2018.pdf'
doc_path = utils.get_relative_file_path(doc)
print(doc_path)
if document_converter.check_if_file_already_converted(doc):
    print("File is already converted")
else:
    print("File is not converted yet")
# text = document_converter.convert_file_from_pdf_to_text(doc_path)
# document_converter.save_text_into_file(text, utils.get_relative_file_path('DnD_BasicRules_2018.txt'))


logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# parser = argparse.ArgumentParser(description='Document Question and Answer System')
# parser.add_argument('-a', '--arg1', type=int, help='Convert document from one format to another')
# parser.add_argument('-b', '--arg2', type=str, help='Description of argument 2')

# args = parser.parse_args()

# if args.arg1:
#     print(f'Argument 1: {args.arg1}')
# if args.arg2:
#     print(f'Argument 2: {args.arg2}')