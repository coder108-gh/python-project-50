from gendiff.files import get_extension


def test_file1():
    assert "" == get_extension('abrakadabra')


def test_file2():
    assert "txt" == get_extension('abrakadabra.txt')


def test_file3():
    assert "rr" == get_extension('abrakadabra.txt.rr')


def test_file4():
    assert "" == get_extension('abrakadabra.txt.')


def test_file5():
    assert "" == get_extension('.github')
