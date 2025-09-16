import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def test_notebook_runs():
    with open("notebooks/E_commerce_project.ipynb") as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb)
