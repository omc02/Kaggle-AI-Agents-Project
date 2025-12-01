import json
import re

# Read the notebook file as text first to see structure
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# Simple string replacement approach - replace all '. ' with '.'
# This needs to be done carefully to avoid breaking strings that should have spaces
fixed_content = content.replace('\. ', '.')

# Write back
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print('✅ Fixed all ". " (dot-space) patterns in the notebook!')

# Verify
with open('capstone_notebook_agentic_ai_kaggle.ipynb', 'r', encoding='utf-8') as f:
    verify_content = f.read()
    count = verify_content.count('\. ')
    print(f'Remaining ". " patterns: {count}')
