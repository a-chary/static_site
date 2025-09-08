import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag= "<p>", value="Test Text", props={"class": "content", "color": "blue"})
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}, value: {node.value}, children: {node.children}, props: {node.props})")
    
    def test_props_to_html(self):
        node = HTMLNode(tag= "<p>", value="Test Text", props={"class": "content", "color": "blue"})
        self.assertEqual(node.props_to_html(), ' class="content" color="blue"')
    
    def test_no_props(self):
        node = HTMLNode(tag= "<p>", value="Test Text")
        self.assertEqual(repr(node), f"HTMLNode(tag: {node.tag}, value: {node.value}, children: {node.children}, props: {node.props})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_plain_text(self):
        node = LeafNode(tag=None, value = "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
class TestParentNode(unittest.TestCase):
    def test_to_html_many_children(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        child4 = LeafNode(None, "Normal text")
        node = ParentNode("p", [child1, child2, child3, child4])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()