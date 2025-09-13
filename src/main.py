import os
import sys

from config import DEST, CONTENT, TEMPLATE
from copy_static import copy_files
from page_generator import generate_pages_recursively


def main():

    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    copy_files()
    cont_path = os.path.abspath(CONTENT)
    template_path = os.path.abspath(TEMPLATE)
    dest_path = os.path.abspath(DEST)
    generate_pages_recursively(cont_path, template_path, dest_path, basepath)


main()