import os.path, glob
import re

def detect_trans_lang_freq( file_path ):
    name = os.path.basename( file_path )
    p = re.compile