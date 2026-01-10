from textnode import *


def main():
    text_node = TextNode("Some dummy text",
                         TextType.CODE_TEXT,
                         "www.google.com")
    print(text_node)
    return 0


if __name__ == "__main__":
    main()