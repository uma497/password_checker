import pytest
from src.password_checker import check_strength

def test_strength_levels():
    assert "Weak" in check_strength("abc")        # too short
    assert "Moderate" in check_strength("abc12345") # medium
    assert "Strong" in check_strength("Abc@12345")  # strong
