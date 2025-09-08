from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # nested markdown not supported by project spec
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            d_count = node.text.count(delimiter)
            # if delimiter not in node text, append to new list and done
            if d_count == 0:
                new_nodes.append(node)
            # raise exception if missing closing delimiter
            elif d_count % 2 != 0:
                raise Exception(f"missing closing {delimiter}")
            else:
                old_text = node.text
                for i in range(d_count // 2):
                    new_text = old_text.split(delimiter, maxsplit = 2)
                    if new_text[0] != '':
                        new_text_node = TextNode(new_text[0], TextType.PLAIN)
                        new_nodes.append(new_text_node)
                    new_special_node = TextNode(new_text[1], text_type)
                    new_nodes.append(new_special_node)
                    if new_text[2] != '' and i == (d_count // 2 - 1):
                        new_text_node_two = TextNode(new_text[2], TextType.PLAIN)
                        new_nodes.append(new_text_node_two)
                    else:
                        old_text = new_text[2]
    return new_nodes
