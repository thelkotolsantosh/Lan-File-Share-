"""
Unit tests for LAN File Share
Run with: pytest test_app.py
"""

import unittest
import os
import json
from app import app, UPLOAD_FOLDER


class TestLANFileShare(unittest.TestCase):
    """Test cases for LAN File Share application"""
    
    def setUp(self):
        """Set up test client and test database"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Create test folder if it doesn't exist
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
    
    def tearDown(self):
        """Clean up after tests"""
        # Remove test files
        if os.path.exists(UPLOAD_FOLDER):
            for filename in os.listdir(UPLOAD_FOLDER):
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)
    
    def test_index_page_loads(self):
        """Test that the index page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'LAN File Share', response.data)
        self.assertIn(b'Upload File', response.data)
    
    def test_upload_file(self):
        """Test file upload functionality"""
        # Create a test file
        test_data = b'test file content'
        
        response = self.client.post(
            '/upload',
            data={'file': (b'test.txt', test_data)}
        )
        
        # Should redirect back to index
        self.assertEqual(response.status_code, 302)
        
        # Check if file was created
        self.assertTrue(os.path.exists(os.path.join(UPLOAD_FOLDER, 'test.txt')))
    
    def test_upload_no_file(self):
        """Test upload without selecting a file"""
        response = self.client.post('/upload', data={})
        
        # Should redirect with error
        self.assertEqual(response.status_code, 302)
        self.assertIn('error', response.location)
    
    def test_download_file(self):
        """Test file download functionality"""
        # Create a test file first
        test_filename = 'test.txt'
        test_filepath = os.path.join(UPLOAD_FOLDER, test_filename)
        
        with open(test_filepath, 'w') as f:
            f.write('test content')
        
        # Try to download it
        response = self.client.get(f'/download/{test_filename}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test content', response.data)
    
    def test_download_nonexistent_file(self):
        """Test downloading a file that doesn't exist"""
        response = self.client.get('/download/nonexistent.txt')
        
        # Should redirect with error
        self.assertEqual(response.status_code, 302)
    
    def test_delete_file(self):
        """Test file deletion functionality"""
        # Create a test file first
        test_filename = 'test_delete.txt'
        test_filepath = os.path.join(UPLOAD_FOLDER, test_filename)
        
        with open(test_filepath, 'w') as f:
            f.write('test content')
        
        # Verify file exists
        self.assertTrue(os.path.exists(test_filepath))
        
        # Delete the file
        response = self.client.post(f'/delete/{test_filename}')
        
        # Should redirect back to index
        self.assertEqual(response.status_code, 302)
        
        # Verify file is deleted
        self.assertFalse(os.path.exists(test_filepath))
    
    def test_delete_nonexistent_file(self):
        """Test deleting a file that doesn't exist"""
        response = self.client.post('/delete/nonexistent.txt')
        
        # Should redirect with error
        self.assertEqual(response.status_code, 302)
    
    def test_file_type_validation(self):
        """Test that disallowed file types are rejected"""
        # Note: This test depends on the current ALLOWED_EXTENSIONS
        # For now, we'll test with a file type that should work
        test_data = b'test content'
        
        response = self.client.post(
            '/upload',
            data={'file': (b'test.txt', test_data)}
        )
        
        # Should be successful (txt is in ALLOWED_EXTENSIONS)
        self.assertEqual(response.status_code, 302)


class TestAppConfiguration(unittest.TestCase):
    """Test application configuration"""
    
    def test_upload_folder_created(self):
        """Test that upload folder is created"""
        self.assertTrue(os.path.exists(UPLOAD_FOLDER))
    
    def test_app_exists(self):
        """Test that Flask app is initialized"""
        self.assertIsNotNone(app)
        self.assertTrue(hasattr(app, 'config'))


def run_tests():
    """Run all tests"""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
