import unittest

from extract import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![image1](https://i.imugr.com/zjjcJKZ.png) and ![image2](https://shorturl.at/GH3DU)"
        )
        self.assertListEqual([("image1", "https://i.imugr.com/zjjcJKZ.png"), ("image2", "https://shorturl.at/GH3DU")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "There is a [link](https://www.example.com) in this text"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)