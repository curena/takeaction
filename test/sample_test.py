from __future__ import print_function
 
def setup_module(module):
    print('\nsetup_module()')
 
def teardown_module(module):
    print('teardown_module()')
 
def setup_function(function):
    print('\nsetup_function()')
 
def teardown_function(function):
    print('\nteardown_function()')
 
def test_1():
    print('-  test_1()')
 
def test_2():
    print('-  test_2()')
 
 
class TestClass:
 
    @classmethod 
    def setup_class(cls):
        print ('\nsetup_class()')
 
    @classmethod 
    def teardown_class(cls):
        print ('teardown_class()')
 
    def setup_method(self, method):
        print ('\nsetup_method()')
 
    def teardown_method(self, method):
        print ('\nteardown_method()')
 
    def test_3(self):
        print('- test_3()')
 
    def test_4(self):
        print('- test_4()')