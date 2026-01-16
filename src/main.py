from textnode import *
from HTMLNode import LeafNode

def main():
    text_node = TextNode("Some dummy text",
                         TextType.CODE_TEXT,
                         "www.google.com")
    print(text_node)
    return 0


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise AttributeError("Text Type is not valid...")


if __name__ == "__main__":
    main()