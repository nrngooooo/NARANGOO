import xml.etree.ElementTree as ET

# create the root element
root = ET.Element("Products")

# create the product element
product = ET.SubElement(root, "Product")
product.set("id", "1001")
product.set("name", "Product 1")
product.set("price", "10")

# create the category element
category = ET.SubElement(product, "Category")
category.text = "Category A"

# create the second product element
product = ET.SubElement(root, "Product")
product.set("id", "1002")
product.set("name", "Product 2")
product.set("price", "20")

# create the category element
category = ET.SubElement(product, "Category")
category.text = "Category B"

# create a new XML file with the above data
tree = ET.ElementTree(root)
tree.write("products.xml")
