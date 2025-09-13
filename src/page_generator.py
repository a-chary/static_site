import os
import re
import sys

from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    title = ''
    for line in lines:
        m = re.match("^#\s(.+)", line)
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
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = read_file(from_path)
    template = read_file(template_path)
    page_content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    page_html = template.replace("{{ Content }}", page_content).replace("{{ Title }}", page_title)
    write_file(dest_path, page_html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if not os.path.isdir(dir_path_content):
        print("content directory not found")
        sys.exit(1)
    
    file_list = os.listdir(dir_path_content)
    if file_list:
        for file in file_list:
            cont_f_path = os.path.join(dir_path_content, file)
            if os.path.isfile(cont_f_path):
                if file.endswith(".md"):
                    output_file = file.replace(".md", ".html")
                    dest_f_path = os.path.join(dest_dir_path, output_file)
                    generate_page(cont_f_path, template_path, dest_f_path)
            elif os.path.isdir(cont_f_path):
                dest_f_path = os.path.join(dest_dir_path, file)
                generate_pages_recursively(cont_f_path, template_path, dest_f_path)