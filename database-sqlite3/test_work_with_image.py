
import pytest

from work_with_image import ImgProcessing

@pytest.fixture
def function_image_processing():
    return ImgProcessing("C:\\Users\\makumar2502\\Documents\\Database\\Screenshot.png")

def test_img_process(function_image_processing):
    assert function_image_processing.process_image() != "Hi World"