def normalize_distance(distance):
    """Normalize distance input to match our data columns."""
    if not distance:
        return None
        
    distance = distance.lower().strip()
    if distance in ['1500', '1500m', '1.5k']:
        return '1500m'
    elif distance in ['mile', 'mi', '1 mile']:
        return 'Mile'
    elif distance in ['5000', '5000m', '5k', '5km']:
        return '5000m'
    elif distance in ['10k', '10km', '10000', '10000m']:
        return '10K'
    elif distance in ['marathon', '42k', '42.2k', '26.2mi']:
        return 'Marathon'
    return None