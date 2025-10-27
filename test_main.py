import pytest
import sys
import subprocess


def test_hello_world_output():
    """Test that main.py outputs 'Hello world?' with a question mark (backwards compatibility)."""
    result = subprocess.run(
        [sys.executable, 'main.py', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello world?", f"Expected 'Hello world?' but got '{result.stdout.strip()}'"


def test_custom_message():
    """Test that custom message argument works."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Custom message', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Custom message", f"Expected 'Custom message' but got '{result.stdout.strip()}'"


def test_help_text():
    """Test that --help displays help text and exits successfully."""
    result = subprocess.run(
        [sys.executable, 'main.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Hello World application' in result.stdout
    assert '--verbose' in result.stdout
    assert '--color' in result.stdout
    assert '--style' in result.stdout


def test_verbose_mode():
    """Test that verbose mode provides additional output."""
    result = subprocess.run(
        [sys.executable, 'main.py', '--verbose', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Running with style:' in result.stdout
    assert 'Color mode:' in result.stdout
    assert 'Hello world?' in result.stdout


def test_color_never():
    """Test that --color never produces plain text output."""
    result = subprocess.run(
        [sys.executable, 'main.py', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    # Should not contain ANSI escape codes
    assert '\x1b[' not in result.stdout
    assert result.stdout.strip() == "Hello world?"


def test_style_success():
    """Test that success style works."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Success message', '--style', 'success', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Success message' in result.stdout


def test_style_warning():
    """Test that warning style works."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Warning message', '--style', 'warning', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Warning message' in result.stdout


def test_style_error():
    """Test that error style works."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Error message', '--style', 'error', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Error message' in result.stdout


def test_combined_arguments():
    """Test combination of multiple arguments."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Test message', '--verbose', '--style', 'success', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Test message' in result.stdout
    assert 'Running with style:' in result.stdout
    assert 'success' in result.stdout


def test_empty_message_edge_case():
    """Test handling of empty string message."""
    result = subprocess.run(
        [sys.executable, 'main.py', '', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    # Empty message should produce empty output (just newline)


def test_special_characters():
    """Test handling of special characters in messages."""
    result = subprocess.run(
        [sys.executable, 'main.py', 'Hello 世界! 🌍', '--color', 'never'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Hello 世界! 🌍' in result.stdout
