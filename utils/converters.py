def time_to_seconds(time_str):
    """Convert time string (MM:SS or HH:MM:SS) to seconds."""
    if not time_str or time_str == '—':
        return None
        
    parts = list(map(float, time_str.replace('+', '').split(':')))
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    return None