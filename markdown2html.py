#!/usr/bin/python3

"""
Markdown to HTML Converter: Converts a Markdown file to HTML.
"""

import sys
import os.path
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """
    Convert Markdown content to HTML and save it to the output file.

    Args:
        markdown_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    # Check if Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown content
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Write HTML content to output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)

    sys.exit(0)

