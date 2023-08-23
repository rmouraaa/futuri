brands = {
    "AGC": ["Vivix", "Guardian", "Cebrace"],
    "Visa": ["Mastercard", "American Express"],
    "Polenghi": ["Tirolez", "Catupiry"]
}

def get_competitors(brand_name):
    """Return the competitors of a given brand."""
    return brands.get(brand_name, [])
