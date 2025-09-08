from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.PLAIN:
            leaf = LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            leaf = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            leaf = LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            leaf = LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            leaf = LeafNode(tag="a", value=text_node.text, props = {"href":text_node.url})
        case TextType.IMAGE:
            leaf = LeafNode(tag="img", value='', props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("invalid text type")
    
    return leaf
