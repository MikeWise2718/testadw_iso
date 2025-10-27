import pytest
import sys
from io import StringIO


def test_hello_world_output(capsys):
    """Test that main.py outputs 'Hello world?' with a question mark."""
    # Import and execute the main module
    import main

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output is exactly "Hello world?" (with newline)
    assert captured.out == "Hello world?\n", f"Expected 'Hello world?\\n' but got '{captured.out}'"
