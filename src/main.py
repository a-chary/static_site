from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    new_node = TextNode("Lord of the Rings", TextType("italic"))
    print(new_node)

main()