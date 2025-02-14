# Obr zobrazhen' 2024/2025 2 semestr

## Install packages
### The simplest way is using virtualenv - not needed fancy envs and package managers
May use any version of 3rd python, but initially it's built on 3.12; 
so another version could cause some compatibility issues

```bash
virtualenv .venv -p py312 
source .venv/bin/activate
pip install -r requirements.txt
```

To check dependencies:
```bash
python check_dependencies.py
```