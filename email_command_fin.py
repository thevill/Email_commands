import os
import subprocess
from pathlib import Path

txt = Path(r'C:\Users\prana\Documents\out.txt').read_text()
txt = txt.replace('\n', '')
if txt == "create folder":
        path = 'C:\\Users\\prana\\Documents\\Email'
        os.chdir(path)
        Newfolder = 'task_1'
        os.makedirs(Newfolder)

