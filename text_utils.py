import textwrap

# Wrap the loaded text( i.e, removing /n and fitting the text in given defined width and again join it)
def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text
