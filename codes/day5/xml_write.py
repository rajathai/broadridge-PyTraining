from xml.dom.minidom import Document

doc = Document()

# Create elements
root = doc.createElement("root")
doc.appendChild(root)
child = doc.createElement("child")
root.appendChild(child)
text = doc.createTextNode("This is a child element")
child.appendChild(text)

# Write to a file
with open("new_file.xml", "w") as f:
    f.write(doc.toprettyxml())

# <?xml version="1.0" ?>
# <root>
# 	<child>This is a child element</child>
# </root>
