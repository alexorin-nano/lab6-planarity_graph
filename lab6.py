import networkx as nx
import matplotlib.pyplot as plt

# Он планарен, но при "кривом" рисовании рёбра могут пересекаться.
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
    ('A', 'E'), ('B', 'E')
])

# 1. Проверка планарности + получение комбинаторной укладки
is_planar, embedding = nx.check_planarity(G)
print("Граф планарен?", is_planar)

if is_planar:
    print("\nКомбинаторная укладка (порядок соседей вокруг каждой вершины):")
    for node, neighbors in embedding.get_data().items():
        print(f"  {node}: {neighbors}")

    # 2. Геометрическая укладка без пересечений
    pos = nx.planar_layout(G)

    # 3. "Рисуем" граф
    plt.figure(figsize=(7, 5))
    nx.draw_networkx(
        G, pos=pos,
        with_labels=True,
        node_color='lightblue',
        node_size=800,
        edge_color='gray',
        width=2
    )
    plt.title("Планарная укладка графа (без пересечений рёбер)")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("planar_drawing.png", dpi=150)
    print("\nРисунок сохранён в planar_drawing.png")
    plt.show()
else:
    # Если граф не планарен, можно получить контрпример (подграф Куратовского)
    print("Граф не планарен. Можно запросить контрпример:")
    # is_planar2, counterexample = nx.check_planarity(G, counterexample=True)
    # print("Контрпример (подграф Куратовского):", counterexample.edges())