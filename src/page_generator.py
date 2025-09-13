import os
import re
import sys

from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    title = ''
    for line in lines:
        m = re.match("^#\s([\w\s]+)", line)
        if m:
            title += m.group(1).strip()
            break

    if title:
        return title
    
    raise Exception("page file has no h1 header")


def read_file(f_path):
    if not os.path.isfile(f_path):
        print(f"no file found at {f_path}")
        sys.exit(1)

    with open(f_path, 'r') as f:
        contents = f.read()
    
    return contents

def write_file(f_path, cont):
    dir = os.path.dirname(f_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)        
    with open(f_path, 'w') as f:
        f.write(cont)
    return
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    source_path = os.path.abspath(from_path)
    markdown = read_file(source_path)

    template_path = os.path.abspath(template_path)
    template = read_file(template_path)

    page_content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    page_html = template.replace("{{ Content }}", page_content).replace("{{ Title }}", page_title)

    write_path = os.path.abspath(dest_path)
    write_file(write_path, page_html)
    return

