def topological_sort(adj_list):
    indegree = {v: 0 for v in adj_list.keys()}
    for vertex in adj_list:
        for neighbor in adj_list[vertex]:
            indegree[neighbor] += 1

    queue = [v for v in indegree if indegree[v] == 0]
    topo_order = []

    while queue:
        vertex = queue.pop(0)
        topo_order.append(vertex)
        for neighbor in adj_list.get(vertex, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


def min_cut_vertices(adj_list, s, t):
    def dfs(vertex, parent, discovery_time, lowest_ancestor, min_cut_vertices):
        nonlocal time
        children = 0
        visited[vertex] = True
        discovery_time[vertex] = time
        lowest_ancestor[vertex] = time
        time += 1

        for neighbor in adj_list[vertex]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                children += 1
                dfs(neighbor, vertex, discovery_time, lowest_ancestor, min_cut_vertices)
                lowest_ancestor[vertex] = min(lowest_ancestor[vertex], lowest_ancestor[neighbor])
                if parent is not None and lowest_ancestor[neighbor] >= discovery_time[vertex]:
                    min_cut_vertices.add(vertex)
            else:
                lowest_ancestor[vertex] = min(lowest_ancestor[vertex], discovery_time[neighbor])

        if parent is None and children > 1:
            min_cut_vertices.add(vertex)

    min_cut_vertices = set()
    visited = {vertex: False for vertex in adj_list.keys()}
    discovery_time = {vertex: 0 for vertex in adj_list.keys()}
    lowest_ancestor = {vertex: 0 for vertex in adj_list.keys()}
    time = 0

    topo_order = topological_sort(adj_list)

    for vertex in topo_order:
        if not visited[vertex]:
            dfs(vertex, None, discovery_time, lowest_ancestor, min_cut_vertices)

    return min_cut_vertices

# Define the adjacency list
adj_list = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11, 12],
    6: [13, 14],
    7: [15, 16],
    8: [17, 18],
    9: [19, 20],
    10: [21, 22],
    11: [23, 24],
    12: [25, 26],
    13: [27, 28],
    14: [29, 30],
    15: [31, 32],
    16: [33, 34],
    17: [35, 36],
    18: [37, 38],
    19: [39, 40],
    20: [41, 42],
    21: [43, 44],
    22: [45, 46],
    23: [47, 48],
    24: [49, 50],
    25: [51, 52],
    26: [53, 54],
    27: [55, 56],
    28: [57, 58],
    29: [59, 60],
    30: [61, 62],
    31: [63, 64],
    32: [65, 66],
    33: [67, 68],
    34: [69, 70],
    35: [71, 72],
    36: [73, 74],
    37: [75, 76],
    38: [77, 78],
    39: [79, 80],
    40: [81, 82],
    41: [83, 84],
    42: [85, 86],
    43: [87, 88],
    44: [89, 90],
    45: [91, 92],
    46: [93, 94],
    47: [95, 96],
    48: [97, 98],
    49: [99, 100],
    50: [101, 102],
    51: [103, 104],
    52: [105, 106],
    53: [107, 108],
    54: [109, 110],
    55: [111, 112],
    56: [113, 114],
    57: [115, 116],
    58: [117, 118],
    59: [119, 120],
    60: [121, 122],
    61: [123, 124],
    62: [125, 126],
    63: [127, 128],
    64: [129, 130],
    65: [131, 132],
    66: [133, 134],
    67: [135, 136],
    68: [137, 138],
    69: [139, 140],
    70: [141, 142],
    71: [143, 144],
    72: [145, 146],
    73: [147, 148],
    74: [149, 150],
    75: [151, 152],
    76: [153, 154],
    77: [155, 156],
    78: [157, 158],
    79: [159, 160],
    80: [161, 162],
    81: [163, 164],
    82: [165, 166],
    83: [167, 168],
    84: [169, 170],
    85: [171, 172],
    86: [173, 174],
    87: [175, 176],
    88: [177, 178],
    89: [179, 180],
    90: [181, 182],
    91: [183, 184],
    92: [185, 186],
    93: [187, 188],
    94: [189, 190],
    95: [191, 192],
    96: [193, 194],
    97: [195, 196],
    98: [197, 198],
    99: [199, 200],
    100: [201, 202],
    731: [1000],
    111: [223, 224],
    112: [225, 226],
    113: [227, 228],
    114: [229, 230],
    115: [231, 232],
    116: [233, 234],
    117: [235, 236],
    118: [237, 238],
    119: [239, 240],
    120: [241, 242],
    121: [243, 244],
    122: [245, 246],
    123: [247, 248],
    124: [249, 250],
    125: [251, 252],
    126: [253, 254],
    127: [255, 256],
    128: [257, 258],
    129: [259, 260],
    130: [261, 262],
    131: [263, 264],
    132: [265, 266],
    133: [267, 268],
    134: [269, 270],
    135: [271, 272],
    136: [273, 274],
    137: [275, 276],
    138: [277, 278],
    139: [279, 280],
    140: [281, 282],
    141: [283, 284],
    142: [285, 286],
    143: [287, 288],
    144: [289, 290],
    145: [291, 292],
    146: [293, 294],
    147: [295, 296],
    148: [297, 298],
    149: [299, 300],
    150: [301, 302],
    151: [303, 304],
    152: [305, 306],
    153: [307, 308],
    154: [309, 310],
    155: [311, 312],
    156: [313, 314],
    157: [315, 316],
    158: [317, 318],
    159: [319, 320],
    160: [321, 322],
    161: [323, 324],
    162: [325, 326],
    163: [327, 328],
    164: [329, 330],
    165: [331, 332],
    166: [333, 334],
    167: [335, 336],
    168: [337, 338],
    169: [339, 340],
    170: [341, 342],
    171: [343, 344],
    172: [345, 346],
    173: [347, 348],
    174: [349, 350],
    175: [351, 352],
    176: [353, 354],
    177: [355, 356],
    178: [357, 358],
    179: [359, 360],
    180: [361, 362],
    181: [363, 364],
    182: [365, 366],
    183: [367, 368],
    184: [369, 370],
    185: [371, 372],
    186: [373, 374],
    187: [375, 376],
    188: [377, 378],
    189: [379, 380],
    190: [381, 382],
    191: [383, 384],
    192: [385, 386],
    193: [387, 388],
    194: [389, 390],
    195: [391, 392],
    196: [393, 394],
    197: [395, 396],
    198: [397, 398],
    199: [399, 400],
    200: [401],
}

s = 1
t = 1000

cut_vertices = min_cut_vertices(adj_list, s, t)
print("The (s,t)-cut vertices are:", ", ".join(map(str, cut_vertices)))

