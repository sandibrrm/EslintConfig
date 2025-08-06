# test_eslintconfig.py
"""
Tests for EslintConfig module.
"""

import unittest
from eslintconfig import EslintConfig

class TestEslintConfig(unittest.TestCase):
    """Test cases for EslintConfig class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EslintConfig()
        self.assertIsInstance(instance, EslintConfig)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EslintConfig()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
