from .encoders import BaseEncoder

def maori_text_to_phonemes(text: str) -> str:
    """Convert Māori text to phonemes"""
    encoder = BaseEncoder()
    return encoder.encode(text)