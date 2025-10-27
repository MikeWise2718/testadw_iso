import argparse
import sys
from rich.console import Console


def main():
    """Main entry point with command-line argument parsing and colored output."""
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Hello World application with argparse and colored output',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Add arguments
    parser.add_argument(
        'message',
        nargs='?',
        default='Hello world?',
        help='Custom message to display (default: "Hello world?")'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output with additional information'
    )

    parser.add_argument(
        '--color',
        choices=['auto', 'always', 'never'],
        default='auto',
        help='Control color output: auto (default), always, or never'
    )

    parser.add_argument(
        '--style',
        choices=['normal', 'success', 'warning', 'error'],
        default='normal',
        help='Output style: normal (default), success, warning, or error'
    )

    # Parse arguments
    args = parser.parse_args()

    # Configure console based on color argument
    if args.color == 'never':
        console = Console(force_terminal=False, no_color=True)
    elif args.color == 'always':
        console = Console(force_terminal=True)
    else:  # auto
        console = Console()

    # Define style mapping
    style_map = {
        'normal': 'white',
        'success': 'green',
        'warning': 'yellow',
        'error': 'red bold'
    }

    # Get the style for the selected output type
    style = style_map[args.style]

    # Print verbose information if requested
    if args.verbose:
        console.print(f"[dim]Running with style: {args.style}[/dim]")
        console.print(f"[dim]Color mode: {args.color}[/dim]")

    # Print the message with the selected style
    console.print(args.message, style=style)


if __name__ == '__main__':
    main()
