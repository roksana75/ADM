# XML 1 - Find the Score

def get_attr_number(node):
    return sum([len(node.items()) for node in tree.iter()])