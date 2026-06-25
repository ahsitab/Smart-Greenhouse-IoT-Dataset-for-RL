import json

with open('aiml505-groupa-smartgreenhouse-gnn-fixed.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

md_cells = []
code_cells = []
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        md_cells.append(''.join(cell['source']))
    elif cell['cell_type'] == 'code':
        code_cells.append(''.join(cell['source']))

print("--- MARKDOWN CELLS ---")
for i, md in enumerate(md_cells[:15]):
    print(f"Cell {i}:\n{md}\n")
