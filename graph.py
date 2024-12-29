import matplotlib.pyplot as plt
import networkx as nx

# Initialize graph
G = nx.DiGraph()

# Define nodes
nodes = {
    "Frontend (React Native)": {"type": "UI"},
    "Frontend (Next.js)": {"type": "UI"},
    "API Gateway (FastAPI)": {"type": "API"},
    "Content Curation Agent": {"type": "Agent"},
    "Question Generator Agent": {"type": "Agent"},
    "Gamification Agent": {"type": "Agent"},
    "Doubt Resolver Agent": {"type": "Agent"},
    "PostgreSQL": {"type": "Database"},
    "Redis (Caching)": {"type": "Cache"},
    "Auth.js": {"type": "Auth"},
    "User": {"type": "User"}
}

# Add nodes to the graph
for node, attributes in nodes.items():
    G.add_node(node, **attributes)

# Define edges
edges = [
    ("User", "Frontend (React Native)"),
    ("User", "Frontend (Next.js)"),
    ("Frontend (React Native)", "API Gateway (FastAPI)"),
    ("Frontend (Next.js)", "API Gateway (FastAPI)"),
    ("API Gateway (FastAPI)", "Content Curation Agent"),
    ("API Gateway (FastAPI)", "Question Generator Agent"),
    ("API Gateway (FastAPI)", "Gamification Agent"),
    ("API Gateway (FastAPI)", "Doubt Resolver Agent"),
    ("Content Curation Agent", "PostgreSQL"),
    ("Question Generator Agent", "PostgreSQL"),
    ("Gamification Agent", "Redis (Caching)"),
    ("Doubt Resolver Agent", "PostgreSQL"),
    ("API Gateway (FastAPI)", "PostgreSQL"),
    ("API Gateway (FastAPI)", "Redis (Caching)"),
    ("Frontend (React Native)", "Auth.js"),
    ("Frontend (Next.js)", "Auth.js")
]

# Add edges to the graph
G.add_edges_from(edges)

# Define node colors based on type
node_colors = []
for node, data in G.nodes(data=True):
    if data['type'] == "UI":
        node_colors.append("lightblue")
    elif data['type'] == "API":
        node_colors.append("orange")
    elif data['type'] == "Agent":
        node_colors.append("lightgreen")
    elif data['type'] == "Database":
        node_colors.append("pink")
    elif data['type'] == "Cache":
        node_colors.append("yellow")
    elif data['type'] == "Auth":
        node_colors.append("purple")
    else:
        node_colors.append("grey")

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold', arrowsize=15)

# Add legend
import matplotlib.patches as mpatches
legend_elements = [
    mpatches.Patch(color="lightblue", label="UI"),
    mpatches.Patch(color="orange", label="API"),
    mpatches.Patch(color="lightgreen", label="Agent"),
    mpatches.Patch(color="pink", label="Database"),
    mpatches.Patch(color="yellow", label="Cache"),
    mpatches.Patch(color="purple", label="Auth")
]
plt.legend(handles=legend_elements, loc="upper left")

plt.title("System Design for Personalized Learning Assistant")
plt.show()
