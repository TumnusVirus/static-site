from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes


# def split_nodes_link(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type != TextType.PLAIN_TEXT:
#             new_nodes.append(node)
#             continue
#         else:
#             pass
#     return new_nodes
