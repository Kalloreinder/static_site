import unittest
from HTMLNode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_same_empty(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        props = node.props_to_html()
        self.assertEqual(props,
                         ' href="https://www.google.com" target="_blank"')
    
    def test_same_not_empty(self):
        node = HTMLNode("a",
                        "Some text in the node",
                        [HTMLNode(), HTMLNode()],
                        {"target": "_blank"}
                    )
        node2 = HTMLNode("a",
                        "Some text in the node",
                        [HTMLNode(), HTMLNode()],
                        {"target": "_blank"}
                    )
        self.assertEqual(node, node2)
    
    def test_not_same(self):
        node = HTMLNode("a",
                        "Some text in the node",
                        [HTMLNode(), HTMLNode()],
                        {"target": "_blank"}
                    )
        node2 = HTMLNode("a",
                        "Some text in the node",
                        [HTMLNode(), HTMLNode(), HTMLNode()],
                        {"target": "_blank"}
                    )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
