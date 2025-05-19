from IPython.display import Image, display


def draw_workflow(graph):
    try:
        img_data = graph.get_graph(xray=True).draw_mermaid_png()
        with open("output.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print("Error:", e)