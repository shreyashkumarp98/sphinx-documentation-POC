#!/usr/bin/env python3
import os

# Create new modules.rst
with open('docs/source/modules.rst', 'w') as f:
    f.write('sphinx-documentation-POC\n')
    f.write('========================\n\n')
    f.write('.. toctree::\n')
    f.write('   :maxdepth: 4\n\n')
    
    # Add all .rst files except index, modules, and conf
    for file in sorted(os.listdir('docs/source')):
        if file.endswith('.rst') and file not in ['index.rst', 'modules.rst', 'conf.rst']:
            module_name = file.replace('.rst', '')
            f.write(f'   {module_name}\n')
