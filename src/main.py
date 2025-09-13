from copy_static import copy_files
from page_generator import generate_page


def main():
    copy_files()
    generate_page("content/index.md", "template.html", "public/index.html")
    return


main()