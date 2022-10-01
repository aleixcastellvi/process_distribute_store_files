import sys

from utils import *

# Input argument 1 of the file main.py
# Directory where the source file is located
source_file_path = sys.argv[1]
 
# Input argument 2 of the file main.py
# Directory where you want to create the root folder of the project
root_path = sys.argv[2]

# Project root folder name. By default it will be "Payments". See code line 43 in utils.py
# project_name = 'Payments'

create_payment_folders(source_file_path, root_path)
