import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node1 = TextNode("Awesome Site", TextType.LINK, url="https://www.google.com")
        node2 = TextNode("Awesome Site", TextType.LINK, url="https://www.google.com")
        self.assertEqual(node1, node2)
    
    def test_unequal_types(self):
        node1 = node1 = TextNode("Awesome Site", TextType.BOLD)
        node2 = TextNode("Awesome Site", TextType.PLAIN)
        self.assertNotEqual(node1, node2)
    
    def test_unequal_text(self):
        node1 = node1 = TextNode("UnAwesome Site", TextType.BOLD)
        node2 = TextNode("Awesome Site", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_unequal_urls(self):
        node1 = node1 = TextNode("Awesome Site", TextType.LINK, url="https://www.wikipedia.org")
        node2 = TextNode("Awesome Site", TextType.LINK, url="https://www.google.com")
        self.assertNotEqual(node1, node2)
    
    def test_unequal_none_url(self):
        node1 = node1 = TextNode("Awesome Site", TextType.LINK)
        node2 = TextNode("Awesome Site", TextType.LINK, url="https://www.google.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
