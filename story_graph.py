#!/usr/bin/env python3
"""
Граф сюжета новеллы «Гарри Поттер и Тени Министерства».
Сцены с новыми картинками (hp_f01–hp_f22) — ветка «Руины в лесу».
"""

import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 12

G = nx.DiGraph()

nodes = {
    "s1": "Платформа 9¾",
    "s2": "Купе поезда",
    "s3": "Незваный гость",
    "s4": "Выбор: Риск",
    "s5A": "Тайный шифр",
    "s5B": "Спрятанный конверт",
    "s6": "Прибытие в замок",
    "s7": "Распределение",
    "s8": "Банкет",
    "s9": "Ночная вылазка",
    "s10": "Запретная секция",
    "s11": "Находка",
    "s12": "Выбор: Доверие",
    "s13A": "Горькая правда",
    "s13B": "Побег от Снейпа",
    "s14": "Урок Зельеварения",
    "s15": "Разговор с Роном",
    "s16": "Предательство?",
    "s17": "Хижина Хагрида",
    "s18": "Появление дементоров",
    "s19": "Магическая дуэль",
    "s20": "Побег в лес",
    "s21": "Встреча с кентаврами",
    "s22": "Заброшенный алтарь",
    "s23": "Голограмма Лили",
    "choiceLily": "Выбор: Куда идти",
    "s24": "Выбор: Альянс",
    "s25A": "Возвращение (с Малфоем)",
    "s25B": "Возвращение (один)",
    "s26": "План проникновения",
    "s27": "Каминная сеть",
    "s28": "Атриум Министерства",
    "s29": "Зал Пророчеств",
    "s30": "Ловушка Директора",
    "s31": "Битва в Министерстве",
    "s32": "Выбор: Финал пути",
    "s33A": "Ложный финал",
    "s33": "Осколки памяти",
    "s34": "Крах заговора",
    "s35": "Дуэль титанов",
    "s36": "Возвращение в Хогвартс",
    "s37": "Последний разговор со Снейпом",
    "s38": "Друзья навсегда",
    "s39": "Финальный взгляд",
    "s40": "Титры",
    "F1": "Тропа к руинам",
    "F2": "Старая ограда",
    "F3": "Развалины башни",
    "F4": "Внутри башни",
    "F5": "Фрески с символами",
    "F6": "Встреча с призраком",
    "F7": "Печать на стене",
    "F8": "Выбор: Печать",
    "F9a": "Воспоминание Лили",
    "F9b": "Обход печати",
    "F10": "Верх башни",
    "F11": "Надпись на камне",
    "F12": "Ключ реагирует",
    "F13": "Шаги снаружи",
    "F14": "Побег с башни",
    "F15": "Погоня в лесу",
    "F16": "Ручей",
    "F17": "Пещера",
    "F18": "Выбор: Путь из леса",
    "F19a": "Ночная дорога",
    "F19b": "Возвращение в замок",
    "F20a": "Окраина Министерства",
    "F20b": "Встреча с друзьями",
    "F21a": "Тайный вход",
    "F21b": "Выбор: Сказать или молчать",
    "F22a": "Подземный зал",
    "F22b": "Тройной союз",
    "F23a": "Выбор: Финал в подземелье",
    "F23b": "Один со знанием",
    "F24a": "Осколки в подземелье",
    "F25a": "Встреча с Дамблдором",
    "e17": "Печать правды",
    "e18": "Тень в подземелье",
    "e19": "Тройной союз (конец)",
    "e20": "Один со знанием (конец)",
}

for nid, label in nodes.items():
    G.add_node(nid, label=label)

edges = [
    ("s1", "s2"), ("s2", "s3"), ("s3", "s4"), ("s4", "s5A"), ("s4", "s5B"),
    ("s5A", "s6"), ("s5B", "s6"), ("s6", "s7"), ("s7", "s8"), ("s8", "s9"),
    ("s9", "s10"), ("s10", "s11"), ("s11", "s12"), ("s12", "s13A"), ("s12", "s13B"),
    ("s13A", "s14"), ("s13B", "s14"), ("s14", "s15"), ("s15", "s16"), ("s16", "s17"),
    ("s17", "s18"), ("s18", "s19"), ("s19", "s20"), ("s20", "s21"), ("s21", "s22"),
    ("s22", "s23"), ("s23", "choiceLily"), ("choiceLily", "s24"), ("choiceLily", "F1"),
    ("s24", "s25A"), ("s24", "s25B"), ("s25A", "s26"), ("s25B", "s26"), ("s26", "s27"),
    ("s27", "s28"), ("s28", "s29"), ("s29", "s30"), ("s30", "s31"), ("s31", "s32"),
    ("s32", "s33A"), ("s32", "s33"), ("s33A", "s40"), ("s33", "s34"), ("s34", "s35"),
    ("s35", "s36"), ("s36", "s37"), ("s37", "s38"), ("s38", "s39"), ("s39", "s40"),
    ("F1", "F2"), ("F2", "F3"), ("F3", "F4"), ("F4", "F5"), ("F5", "F6"),
    ("F6", "F7"), ("F7", "F8"), ("F8", "F9a"), ("F8", "F9b"), ("F9a", "F10"), ("F9b", "F10"),
    ("F10", "F11"), ("F11", "F12"), ("F12", "F13"), ("F13", "F14"), ("F14", "F15"),
    ("F15", "F16"), ("F16", "F17"), ("F17", "F18"), ("F18", "F19a"), ("F18", "F19b"),
    ("F19a", "F20a"), ("F19b", "F20b"), ("F20a", "F21a"), ("F20b", "F21b"),
    ("F21a", "F22a"), ("F21b", "F22b"), ("F21b", "F23b"), ("F22a", "F23a"),
    ("F23a", "F24a"), ("F23a", "F25a"), ("F24a", "e17"), ("F25a", "e18"),
    ("F22b", "e19"), ("F23b", "e20"),
]

for u, v in edges:
    G.add_edge(u, v)

forest_nodes = {"F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9a", "F9b",
                "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18",
                "F19a", "F19b", "F20a", "F20b", "F21a", "F21b", "F22a", "F22b",
                "F23a", "F23b", "F24a", "F25a", "e17", "e18", "e19", "e20"}
choice_nodes = {"s4", "s12", "choiceLily", "s24", "s32", "F8", "F18", "F21b", "F23a"}
end_nodes = {"s40", "e17", "e18", "e19", "e20"}

def hierarchical_layout(G, root="s1"):
    """Раскладка: слева направо по топологическому порядку, узлы в столбцах."""
    topo = list(nx.topological_sort(G))
    level = {}
    for node in topo:
        preds = list(G.predecessors(node))
        if not preds:
            level[node] = 0
        else:
            level[node] = 1 + max(level[p] for p in preds)

    by_level = {}
    for node, lvl in level.items():
        by_level.setdefault(lvl, []).append(node)

    pos = {}
    col_spacing = 2.4 / 5
    row_spacing = 1.8 / 5
    for lvl in sorted(by_level.keys()):
        nodes_in_level = by_level[lvl]
        n = len(nodes_in_level)
        x = lvl * col_spacing
        for i, node in enumerate(nodes_in_level):
            y = (i - (n - 1) / 2) * row_spacing
            pos[node] = (x, y)
    return pos

pos = hierarchical_layout(G)

fig, ax = plt.subplots(figsize=(42, 24), facecolor="#0e0e20")
ax.set_facecolor("#0e0e20")

node_colors = []
for n in G.nodes():
    if n in forest_nodes:
        node_colors.append("#4a7c59")
    elif n in choice_nodes:
        node_colors.append("#8b7355")
    elif n in end_nodes:
        node_colors.append("#9b4d4d")
    else:
        node_colors.append("#3d5a80")

nx.draw_networkx_edges(G, pos, edge_color="#6a7a9a", alpha=0.75, arrows=True,
                       arrowsize=22, connectionstyle="arc3,rad=0.05", ax=ax, width=2)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=4800,
                       alpha=0.95, edgecolors="#9aabbc", linewidths=2, ax=ax)

node_list = list(G.nodes())
name_to_id = {n: i + 1 for i, n in enumerate(node_list)}
num_labels = {n: str(name_to_id[n]) for n in node_list}
nx.draw_networkx_labels(G, pos, num_labels, font_size=16, font_color="white",
                        font_weight="bold", font_family="sans-serif", ax=ax)

ax.set_title("Граф сюжета: Гарри Поттер и Тени Министерства", fontsize=22,
             color="white", pad=24)
ax.axis("off")
plt.tight_layout()
plt.savefig("story_graph.png", dpi=150, facecolor="#0e0e20", edgecolor="none",
            bbox_inches="tight")
plt.close()
print("Сохранено: story_graph.png")
