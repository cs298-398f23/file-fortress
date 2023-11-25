import pytest
from src.StorageManagers import LocalStorageManager
from unittest.mock import Mock, patch


class LocalStorageManagerTest(LocalStorageManager):
    def __init__(self,dict:dict = {}):
        super().__init__(db_returns(dict), "")


class db_returns():
    def __init__(self,val:dict = {}):
        val['id'] = 0
        self.val = val
        pass
    def cursor(self):
        return self
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return None
    def execute(self,query, *args):
        return None
    def fetchone(self):
        return self.val

def test_StorageManager():
    manager = LocalStorageManagerTest()
    
def test_none_raises_file_not_found():
    manager = LocalStorageManagerTest()
    with pytest.raises(FileNotFoundError):
        manager.lookup_link('test.png')

def test_lookup_link():
    manager = LocalStorageManagerTest({'url':'test.png'})
    assert manager.lookup_link('test.png') == 'test.png'


def test_allocate_url():
    manager = LocalStorageManagerTest()
    assert manager.allocate_url('test','test.png') == 'test/test.png'


def test_allocate_url_with_exisiting_file():
    
    mock = Mock()
    mock.side_effect = [True,False] # the first call will return True, and the second will return False
    with patch('src.StorageManagers.Path.exists',mock):
        manager = LocalStorageManagerTest()
        assert manager.allocate_url('test','test.png') == 'test/test.png_1'
