# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    [depth(element, level) for element in elem.getchildren()]
    maxdepth = level if level > maxdepth else maxdepth
    return maxdepth