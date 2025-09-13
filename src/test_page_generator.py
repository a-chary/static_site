import unittest

from page_generator import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_hello(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")
    
    def test_multiline(self):
        md = """

# Hello World

        
This is some content for a page, that has a title.
    """
        title = extract_title(md)
        self.assertEqual(title, "Hello World")
    
    def test_multiline_image_first(self):
        md = """
![your mom, fully naked](https://www.yourmom.com)

# Hello World
        
This is some content for a page, that has a title and an image.
    """
        title = extract_title(md)
        self.assertEqual(title, "Hello World")

    def test_multiline_other_headers(self):
        md = """
### This page is dedicated to the memory of your mom.

# Hello World

#### But it just doesn't do her justice.
        
This is some content for a page, that has a few headers.
    """
        title = extract_title(md)
        self.assertEqual(title, "Hello World")