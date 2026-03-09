
from inline_markdown import extract_markdown_images, extract_markdown_links

import unittest

from text_node import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)