import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag= "<p>", value="Test Text", props={"class": "content", "color": "blue"})
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}, value: {node.value}, children: {node.children}, props: {node.props})")
    
    def test_props_to_html(self):
        node = HTMLNode(tag= "<p>", value="Test Text", props={"class": "content", "color": "blue"})
        self.assertEqual(node.props_to_html(), 'class="content" color="blue" ')
    
    def test_no_props(self):
        node = HTMLNode(tag= "<p>", value="Test Text")
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}, value: {node.value}, children: {node.children}, props: {node.props})")

if __name__ == "__main__":
    unittest.main()