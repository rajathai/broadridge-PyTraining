import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")
root = tree.getroot()

# Root
print(root.tag)

# Len of Root
print(len(root))


# Access 1st Root Child
print(root[0].tag)

# Access len of 1st Root Child
print(len(root[0]))

# Loop over the Root Childeren
for child in root:
    print(child[0].text)
    print(child[1].text)
    print(child[2].text)
    print(child[3].text)

# Rajath
# Kumar
# rajathkumarks@gmail.com
# Thought Leader
# Elon
# Musk
# elon.musk@gmail.com
# CEO


# Root - Children - GrandChildren
print(root[0][0].tag)  # firstname
print(root[0][0].text)  # Rajath

print(root[1][2].text)  # elon.musk@gmail.com


# Get an Attribute
print(root.attrib)  # {'company': 'tesla'}


# Loop over 'email' Tag
for mailid in root.iter("email"):
    print(mailid.text)

# rajathkumarks@gmail.com
# elon.musk@gmail.com

# Find 1st Root Child with how many 'lastname' Tag
print(len(root[0].findall("lastname")))

# Printing the 1st root child with 'lastname' Tag
print(root[0].findall("lastname")[0].text)  # Kumar
print(root[0].findall("lastname")[1].text)  # KS

# Change the email address of Elon
root[1][2].text = "elon.musk@company.com"

# Remove the extra last name in the 1st root child
root[0].remove(root[0].findall("lastname")[1])
tree.write("xml_altered.xml")
