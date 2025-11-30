import json
import re

# Read the notebook
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# List of fixes to apply - fix all '. ' patterns (dot space)
fixes = [
    (r'\. ', '.'),  # Replace all '. ' with '.'
]

# Apply fixes to all cells
for cell in notebook['cells']:
    if cell['cell_type'] in ['code', 'markdown']:
        source = cell['source']
        if isinstance(source, list):
            source = ''.join(source)
        else:
            source = str(source)
        
        # Apply each fix
        for pattern, replacement in fixes:
            source = re.sub(pattern, replacement, source)
        
        # Split back into lines if it was a list
        if isinstance(cell['source'], list):
            cell['source'] = source.split('\n')
            # Add back newlines except for the last one if it was there
            for i in range(len(cell['source'])-1):
                cell['source'][i] = cell['source'][i] + '\n'
        else:
            cell['source'] = source

# Write the fixed notebook
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print('✅ Fixed all spacing issues in the notebook!')
