import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    clean_block_list = [block.strip() for block in block_list if block != ""]
    return clean_block_list

def is_quote(lines):
    for line in lines:
        if line[0] != '>':
            return False
    return True

def is_ul(lines):
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def is_ol(lines):
    i = 1
    for line in lines:
        m = re.match(r"(\d+)\.\s", line)
        if m is None:
            return False
        if int(m.group(1)) != i:
            return False
        i += 1
    return True

def block_to_block_type(block):
    if re.match(r"#{1,6}\s", block):
        return BlockType.HEADING
    
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    block_lines = block.split('\n')

    if is_quote(block_lines):
        return BlockType.QUOTE
    
    if is_ul(block_lines):
        return BlockType.UNORDERED_LIST
    
    if is_ol(block_lines):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    

    

