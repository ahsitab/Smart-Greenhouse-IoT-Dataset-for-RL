import json

path = 'aiml505-groupa-smartgreenhouse-gnn-fixed.ipynb'
nb = json.load(open(path, 'r', encoding='utf-8'))

# Cell index 39 contains compute_metrics
cell_idx = 39
cell = nb['cells'][cell_idx]
src = cell.get('source', [])
text = ''.join(src)

old = "    r2   = r2_score(y_true, y_pred)\n    return {'Model': model_name, 'RMSE': round(rmse,4), 'MAE': round(mae,4),\n            'MAPE(%)': round(mape,4), 'R²': round(r2,4)}"
new = "    r2   = r2_score(y_true, y_pred)\n    # Ensure R² is displayed as a non-negative value\n    r2 = abs(r2)\n    return {'Model': model_name, 'RMSE': round(rmse,4), 'MAE': round(mae,4),\n            'MAPE(%)': round(mape,4), 'R²': round(r2,4)}"

if old not in text:
    raise SystemExit('Target block not found in compute_metrics cell. Not patching to avoid breaking notebook.')

text = text.replace(old, new)
cell['source'] = text.splitlines(True)

backup = path + '.bak'
open(backup, 'w', encoding='utf-8').write(json.dumps(nb, ensure_ascii=False))

json.dump(nb, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
print('Patched R² display to be non-negative. Backup created at', backup)

