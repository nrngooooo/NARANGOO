graph_list = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

graph_list["E"] = []  
graph_list["A"].append("E")

print(graph_list)

graph_matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

for i in range(len(graph_matrix)):
    graph_matrix[i].append(0)
graph_matrix.append([0] * (len(graph_matrix) + 1))
graph_matrix[0][-1] = 1 

print(graph_matrix)
