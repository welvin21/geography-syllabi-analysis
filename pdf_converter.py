#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tika
import os
from tika import parser as tika_parser
tika.initVM()


# In[23]:


class PDFToText():
    def __init__(self):
        self.engine = tika_parser
    
    def convert(self, file_path):
        if not os.path.isfile(file_path): 
            raise Exception("Invalid file path!")
        
        parsed_pdf = self.engine.from_file(file_path)
        return parsed_pdf["content"]


# In[ ]:




