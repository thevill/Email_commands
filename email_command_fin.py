#created by Pranay Wajjala
#greenscizor

import os
import subprocess
from pathlib import Path

txt = Path(r'path-to-output-text-file').read_text()
txt = txt.replace('\n', '')
if txt == "create folder":
        path = 'path-to-the-folder'
        os.chdir(path)
        Newfolder = 'your-folder-name'
        os.makedirs(Newfolder)
