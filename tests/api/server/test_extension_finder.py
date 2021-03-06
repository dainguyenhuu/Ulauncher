import os
from ulauncher.api.server.extension_finder import find_extensions


def test_find_extensions__test_extension__is_found():
    ext_dir = os.path.dirname(os.path.abspath(__file__))
    (id, path) = list(find_extensions(ext_dir))[0]
    assert id == 'test_extension'
    assert path == '%s/test_extension' % ext_dir
