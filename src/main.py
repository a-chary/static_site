import os
import sys

from copy_static import copy_files
from page_generator import generate_pages_recursively


def main():

    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    copy_files()
    cont_path = os.path.abspath("content/")
    template_path = os.path.abspath("template.html")
    dest_path = os.path.abspath("docs/")
    generate_pages_recursively(cont_path, template_path, dest_path, basepath)


main()