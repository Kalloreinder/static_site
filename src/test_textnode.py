import unittest
from textnode import TextNode, TextType
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN, "www.google.com")
        node2 = TextNode("This is a text node", TextType.PLAIN, "www.google.com")
        self.assertEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN, "www.google.com")
        node2 = TextNode("This is a text node", TextType.PLAIN, "www.apple.com")
        self.assertNotEqual(node, node2)
    
    def test_text_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
    
    def test_unexisting_type(self):
        with self.assertRaises(AttributeError):
            node = TextNode("This is a text node", TextType.UNDERSCORE)
            html_node = text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
