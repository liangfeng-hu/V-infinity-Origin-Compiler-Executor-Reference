"""
Import shim to allow running demo.py directly from repository layout.

Layout:
  reference-impl/python/gate91_reference.py
  reference-impl/python/lse_reference.py

Exports:
  gate91, lse
"""

import importlib.util
from pathlib import Path


def _load(module_name: str, file_name: str):
    here = Path(__file__).resolve().parent
    path = here / file_name
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


gate91 = _load("gate91_reference", "gate91_reference.py")
lse = _load("lse_reference", "lse_reference.py")
