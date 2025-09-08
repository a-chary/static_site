import unittest

from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold_text(self):
        node = TextNode("This is important text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is important text")
    
    def test_it_text(self):
        node = TextNode("This is important text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is important text")
    
    def test_code_text(self):
        node = TextNode("Some javascript probably", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Some javascript probably")
    
    def test_code_link(self):
        node = TextNode("Teh best website", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Teh best website")
        self.assertEqual(html_node.props, {"href": "https://google.com"})
    
    def test_code_image(self):
        node = TextNode("Your mom, fully naked", TextType.IMAGE, "https://sugargeekshow.com/wp-content/uploads/2022/08/vanilla_cupcake_featured_blog.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://sugargeekshow.com/wp-content/uploads/2022/08/vanilla_cupcake_featured_blog.jpg", "alt": "Your mom, fully naked"})
