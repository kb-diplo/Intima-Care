from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
def markdown_to_html(text):
    """Convert markdown text to HTML"""
    if not text:
        return ''
    
    # Configure markdown with extensions for better formatting
    md = markdown.Markdown(extensions=[
        'markdown.extensions.nl2br',  # Convert newlines to <br>
        'markdown.extensions.fenced_code',  # Support for code blocks
        'markdown.extensions.tables',  # Support for tables
    ])
    
    html = md.convert(text)
    return mark_safe(html)
