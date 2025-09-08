class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        # children is a list of child nodes
        self.children = children
        # props is a dictionary of attributes, ie {"href" : "https://www.google.com", ...}
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        attr = ''
        if self.props is not None:
            for k,v in self.props.items():
                attr += ' ' + k + '="' + v + '"'
        return attr
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node has no value")
        if self.tag is None:
            return self.value
        html_string = '<' + self.tag + self.props_to_html() + '>' + self.value + '</' + self.tag + '>'
        return html_string         
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        # note leaf nodes will never be passed to parent node .to_html method
        if not self.tag:
            raise ValueError("parent node has no tag")
        if not self.children:
            raise ValueError("parent node has no children")
        
        html_string = ''
        for child in self.children:
            # note: if node is leaf node automatically calls to leaf node .to_html method, only parent node
            # call is recursive (and parent nodes automatically call to parent node .to_html)
            html_string += child.to_html()
        # all content is in leaf (child) nodes, so formatt between parent tags for each parent node
        return '<' + self.tag + '>' + html_string + '</' + self.tag + '>'