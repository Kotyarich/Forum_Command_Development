def make_human_readable(obj, attrs):
    attrs_str = ', '.join([f'{attr}={getattr(obj, attr)}' for attr in attrs])
    return f'{type(obj).__name__}({attrs_str})'
