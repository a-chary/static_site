class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        # props is a dictionary of attributes, ie {"href" : "https://www.google.com", ...}
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        attr = ''
        for k,v in self.props.items():
            attr += k + '="' + v + '" '
        return attr
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"