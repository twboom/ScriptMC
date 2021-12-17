__version__ = '0.0.1'

from trimmer import Trimmer


print(f'ScriptMC v{__version__}')

with open('./test/test.scriptmc', 'r') as f:
    text = f.read()

trimmer = Trimmer(text)
trimmer.trim()

print("\n \n \n")

print(trimmer)