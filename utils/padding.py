"""
Utility functions for padding text.
text: str - The text to be padded.
pad_top: int - Number of newlines to add at the top.
pad_bottom: int - Number of newlines to add at the bottom.
return: str - The padded text.
"""


def padding(text: str, pad_top: int = 4, pad_bottom: int = 4) -> str:
    """Add padding to the text."""
    pad_top_str = "\n" * pad_top
    pad_bottom_str = "\n" * pad_bottom
    return f"{pad_top_str}{text}{pad_bottom_str}"
