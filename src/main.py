import os

from copy_static import copy_files
from page_generator import generate_pages_recursively


def main():
    copy_files()
    cont_path = os.path.abspath("content/")
    template_path = os.path.abspath("template.html")
    dest_path = os.path.abspath("public/")
    generate_pages_recursively(cont_path, template_path, dest_path)


main()