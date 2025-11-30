import json
import re

# Read the notebook
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# List of fixes to apply
fixes = [
    (r'dataframe\. copy', 'dataframe.copy'),
    (r'self\. df', 'self.df'),
    (r"IsActiveMember\]\. sum", "IsActiveMember'].sum"),
    (r'observed=True\). agg', 'observed=True).agg'),
    (r'pd\. DataFrame', 'pd.DataFrame'),
    (r'\]\. sort_values', '].sort_values'),
    (r'high_risk\. head', 'high_risk.head'),
    (r"Balance\]\. mean", "Balance'].mean"),
    (r'key\. replace', 'key.replace'),
    (r'self\. insights', 'self.insights'),
    (r"segments\]\. head", "segments'].head"),
    (r'gen\. configure', 'gen.configure'),
    (r'self\.chat_session\. send_message', 'self.chat_session.send_message'),
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
