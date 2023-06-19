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


def printTree(node, depth=0):
    if len(node["children"]) == 0:
        print(" " * depth + str(node["value"]))
    else:
        print(" " * depth + str(node["value"]))
        for child in node["children"]:
            printTree(child, depth=depth+4)


printTree(t)