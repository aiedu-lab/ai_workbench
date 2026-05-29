# tests/conftest.py
# Shared fixtures and path setup for pytest.

import sys
import os

# Allow tests to import from the project root without installing the package.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
