from gendiff.files import get_file_extention


def test_file1():
    assert "" == get_file_extention('abrakadabra')


def test_file2():
    assert "txt" == get_file_extention('abrakadabra.txt')


def test_file3():
    assert "rr" == get_file_extention('abrakadabra.txt.rr')


def test_file4():
    assert "" == get_file_extention('abrakadabra.txt.')


def test_file5():
    assert "" == get_file_extention('.github')
