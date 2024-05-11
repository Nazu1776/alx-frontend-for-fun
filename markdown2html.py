#!/usr/bin/python3

import sys
import os

def markdown2html(markdown_file, output_file):
    """
    Convert Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.
    """
    # Check if Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Perform the conversion and write to the output file
    with open(markdown_file, 'r') as md:
        markdown_content = md.read()
        html_content = "<html><body>" + markdown_content + "</body></html>"
        with open(output_file, 'w') as html:
            html.write(html_content)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown2html(markdown_file, output_file)

    sys.exit(0)

