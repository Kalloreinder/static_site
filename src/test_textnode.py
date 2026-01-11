import unittest
from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
