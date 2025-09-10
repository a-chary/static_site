from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # nested markdown not supported by project spec
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            d_count = node.text.count(delimiter)
            # if delimiter not in node text, append to new list and done
            if d_count == 0:
                new_nodes.append(node)
            # raise exception if missing closing delimiter
            elif d_count % 2 != 0:
                raise Exception(f"missing closing {delimiter}")
            else:
                old_text = node.text
                for i in range(d_count // 2):
                    new_text = old_text.split(delimiter, maxsplit = 2)
                    if new_text[0] != '':
                        new_text_node = TextNode(new_text[0], TextType.PLAIN)
                        new_nodes.append(new_text_node)
                    new_special_node = TextNode(new_text[1], text_type)
                    new_nodes.append(new_special_node)
                    if new_text[2] != '' and i == (d_count // 2 - 1):
                        new_text_node_two = TextNode(new_text[2], TextType.PLAIN)
                        new_nodes.append(new_text_node_two)
                    else:
                        old_text = new_text[2]
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        old_text = node.text
        for match in matches:
            # extract alt_text and url
            alt_text, url = match
            # split text on image markdown
            new_text = old_text.split(f"![{alt_text}]({url})", maxsplit = 1)
            if new_text[0] != '':
                new_nodes.append(TextNode(new_text[0], TextType.PLAIN))
            # create new image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            old_text = new_text[1]
        if old_text != '':
            new_nodes.append(TextNode(old_text, TextType.PLAIN))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        old_text = node.text
        for match in matches:
            # extract alt_text and url
            text, url = match
            # split text on link markdown
            new_text = old_text.split(f"[{text}]({url})", maxsplit = 1)
            if new_text[0] != '':
                new_nodes.append(TextNode(new_text[0], TextType.PLAIN))
            # create new link node
            new_nodes.append(TextNode(text, TextType.LINK, url))
            old_text = new_text[1]
        if old_text != '':
            new_nodes.append(TextNode(old_text, TextType.PLAIN))
    return new_nodes

def text_to_textnodes(text):
    node_list = [TextNode(text, TextType.PLAIN)]
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list