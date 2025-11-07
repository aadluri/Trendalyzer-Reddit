from src.data_processing.color_analysis import extract_dominant_colors
import os

def test_color_extraction():
    test_image = "data/images/test.jpg"
    if not os.path.exists(test_image):
        return  # skip if no test image
    colors = extract_dominant_colors(test_image)
    assert isinstance(colors, list)
    assert len(colors) > 0
