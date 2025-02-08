import unittest
from app.services.ocr_service import extract_text

class TestExtractText(unittest.TestCase):

    def test_extract_text_valid_image(self):
        # Test with a valid image file
        result = extract_text('path/to/valid/image.png')
        self.assertIsInstance(result, str)  # Expecting a string output

    def test_extract_text_invalid_image(self):
        # Test with an invalid image file
        with self.assertRaises(ValueError):
            extract_text('path/to/invalid/image.txt')

    def test_extract_text_empty_image(self):
        # Test with an empty image
        result = extract_text('path/to/empty/image.png')
        self.assertEqual(result, '')  # Expecting empty string output

if __name__ == '__main__':
    unittest.main()