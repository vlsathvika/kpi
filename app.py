import os
import subprocess
import streamlit as st

# Clone the private repository using subprocess to avoid gitpython issues
if not os.path.exists('kpi_generator'):
    subprocess.run(['git', 'clone', f'https://{os.getenv("GITHUB_TOKEN")}@github.com/vlsathvika/kpi-generator.git', 'kpi_generator'], check=True)

# Import your code from the cloned repository
import kpi_generator.code_1 as code_1 

exec(open('kpi_generator/code_1.py').read())
