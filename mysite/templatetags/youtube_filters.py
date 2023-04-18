from django import template
import re

register = template.Library()


@register.filter
def get_youtube_id(value):
    youtube_id_match = re.search(
        r'(?:(?:v=|\/embed\/)|(?:youtu.be\/|v\/|u\/\w\/|embed\/watch\?v=|\&v=|\%3D|%2F[\w\-%]+%2F))(?P<id>[\w\-%]{11})', value)
    if youtube_id_match:
        return youtube_id_match.group('id')
    return None
