import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_to_html_b(self):
        # Create a bold leaf node
        node = LeafNode("b", "Bold text")
        # Assert that the rendered HTML is exactly what we expect
        self.assertEqual(node.to_html(), "<b>Bold text</b>")
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_no_children(self):
        # Testing that it works for other tags like 'i' (italics)
        node = LeafNode("i", "italic text")
        self.assertEqual(node.to_html(), "<i>italic text</i>")

if __name__ == "__main__":
    unittest.main()