# test_pancakerouter.py
"""
Tests for PancakeRouter module.
"""

import unittest
from pancakerouter import PancakeRouter

class TestPancakeRouter(unittest.TestCase):
    """Test cases for PancakeRouter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PancakeRouter()
        self.assertIsInstance(instance, PancakeRouter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PancakeRouter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
