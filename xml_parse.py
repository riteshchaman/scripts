import sys, getopt
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

def printprop(filename, root):
        list_props = []
        for prop in root.getchildren():
                prop_name = prop.find('name')
                if prop_name is not None:
                        element = str(prop_name.text) + "=|" + str(prop.find('value').text) + "|"
                        list_props.append(element)
        if len(list_props) > 0:
                list_props.sort()
                for item in list_props:
                        print item


if len(sys.argv) < 2:
        print "Usage: python " + sys.argv[0] + " <xml file name>"
        exit(1)

xml_file = sys.argv[1]

conf = ElementTree.parse(xml_file).getroot()
printprop(xml_file, root = conf)

