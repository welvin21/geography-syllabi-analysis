import tika
import os
from tika import parser as tika_parser
tika.initVM()

class PDFToText():
    def __init__(self):
        self.engine = tika_parser
    
    def convert(self, file_path):
        if not os.path.isfile(file_path): 
            raise Exception("Invalid file path!")
        
        parsed_pdf = self.engine.from_file(file_path)
        return parsed_pdf["content"]
