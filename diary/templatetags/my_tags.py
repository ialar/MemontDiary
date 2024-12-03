import re

from django import template

register = template.Library()


@register.simple_tag
def my_media_tag(data):
    if data:
        return f"/media/{data}"
    return "#"


@register.filter
def highlight(text, query):
    if query:
        # Добавляем <span class="highlight"> вокруг совпадений
        highlighted_text = re.sub(
            f"({re.escape(query)})",  # Экранируем запрос для безопасности
            r'<span class="highlight">\1</span>',  # Оборачиваем совпадение
            text,
            flags=re.IGNORECASE,  # Игнорируем регистр
        )
        return highlighted_text
    return text
