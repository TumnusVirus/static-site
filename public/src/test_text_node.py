import unittest

from text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_type_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node,node2)
    
    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node,node2)

    def test_url_eq(self):
        node = TextNode("This is a text node",TextType.BOLD,url="https://www.google.com")
        node2 = TextNode("This is a text node",TextType.BOLD,url="https://www.google.com")
        self.assertEqual(node,node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node",TextType.BOLD,url="https://www.google.com")
        node2 = TextNode("This is a text node",TextType.BOLD)
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()