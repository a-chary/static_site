from block import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from split import text_to_textnodes
from text_to_html import text_node_to_html_node


def text_to_html_nodes(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def p_block(block):
    p_text = block.replace('\n', ' ')
    if p_text == '':
        return None
    child_nodes = text_to_html_nodes(p_text)
    new_node = ParentNode(tag="p", children = child_nodes)
    return new_node


def h_block(block):
    i = 0
    for char in block:
        if char == '#':
            i += 1
        if char != '#':
            break
    if i > 6:
        i = 6
    h_tag = 'h' + str(i)
    h_text = block[i:-i].strip()
    if h_text == '':
        return None
    child_nodes = text_to_html_nodes(h_text)
    new_node = ParentNode(tag=h_tag, children = child_nodes)
    return new_node


def c_block(block):
    c_text = block[4:-3]
    child = [LeafNode(tag="code", value=c_text),]
    new_node = ParentNode(tag="pre", children = child)
    return new_node


def q_block(block):
    clean_quote = []
    quote_lines = block.split('\n')
    for line in quote_lines:
        clean_line = line[1:].strip()
        if clean_line != '':
            clean_quote.append(clean_line)
    if not clean_quote:
        return None
    q_text = ' '.join(clean_quote)
    child_nodes = text_to_html_nodes(q_text)
    new_node = ParentNode(tag="blockquote", children = child_nodes)
    return new_node


def block_node_logic(block, type):
    if type == BlockType.PARAGRAPH:
        return p_block(block)
    if type == BlockType.HEADING:
        return h_block(block)
    if type == BlockType.CODE:
        return c_block(block)
    if type == BlockType.QUOTE:
        return q_block(block)
    


def markdown_to_html_node(markdown):
    # convert markdown to blocks
    markdown_blocks = markdown_to_blocks(markdown)
    block_nodes = []
    # loop over each block
    for block in markdown_blocks:
        # determine block type
        if block is None or block.isspace():
            continue
        block_type = block_to_block_type(block)
        # based on block type, create html node with proper data
        block_node = block_node_logic(block, block_type)
        if block_node:
            block_nodes.append(block_node)
    div_node = ParentNode(tag="div", children = block_nodes)
    return div_node


