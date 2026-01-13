import unittest
from HTMLNode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
    
    def test_leaf_no_children(self):
        node = LeafNode("p", "Hello World!", [HTMLNode()])
        self.assertRaises(ValueError)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
        print(parent_node.to_html())

if __name__ == "__main__":
    unittest.main()
