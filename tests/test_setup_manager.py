import pytest
from ..newpy.setup_manger import PrepareSetup


class TestPrepareSetup:

    ps = PrepareSetup()

    @pytest.fixture(scope="function")
    def info(self):
        print('\nEnter: gal')

    def test_get_personaldata(self):
        assert isinstance(self.ps._get_personaldata(), dict)
        assert self.ps._get_personaldata() == {
            'author': 'StefPy',
            'email': 'stefan.mail.sk@gmail.com',
            'year': '2020'
        }

    def test_item_no_entry(self):
        line = 'name="pkg-YOUR-USERNAME-HERE",'
        assert self.ps._item(line,
                             "author",
                             "pkg-YOUR-USERNAME-HERE",
                             prefix="pkg-",
                             git=True) == ('pkg-YOUR-USERNAME-HERE',
                                           'pkg-StefPy')

    def test_item_with_entry(self, info):
        line = 'name="pkg-YOUR-USERNAME-HERE",'
        assert self.ps._item(line,
                             "author",
                             "pkg-YOUR-USERNAME-HERE",
                             prefix="pkg-",
                             git=True) == ('pkg-YOUR-USERNAME-HERE', 'gal')
