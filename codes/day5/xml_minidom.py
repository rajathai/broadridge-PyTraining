from xml.dom import minidom

# Load and parse an XML file
dom = minidom.parse("employee.xml")

# Getting elements
elements = dom.getElementsByTagName("firstname")
for elem in elements:
    print(elem.firstChild.data)
