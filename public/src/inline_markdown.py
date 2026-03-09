import re
from text_node import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("...")
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section,TextType.TEXT))
            else:
                new_nodes.append(TextNode(section,text_type))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)