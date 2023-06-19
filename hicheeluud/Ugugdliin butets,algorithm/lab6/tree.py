from treelib import Tree
t = {
    "value": "Есүхэй Баатар",
    "children": [
        {
            "value": "Тэмүгэ",
            "children": []
        },
        {
            "value": "Тэмүүжин",
            "children": [
                {"value": 'Зүчи', "children": []},
                {"value": 'Тулуй', "children": []},
                {"value": 'Цагаадай', "children": []},
                {"value": 'Өгөөдэй', "children": [
                        {"value": 'Гүюүг', "children": []} 
                        ]},
            ],
        },
        {"value": 'Тэмүүлэн', "children": []},
        {"value": 'Хасар', "children": []},
    ],
}


tree = Tree()
tree.create_node(t['value'], t['value'])


def add_node_to_tree(node, parent_id):
    for child in node['children']:
        child_value = child['value']
        child_id = f'{parent_id}/{child_value}'
        tree.create_node(child_value, child_id, parent=parent_id)
        add_node_to_tree(child, child_id)


add_node_to_tree(t, t['value'])
tree.show()