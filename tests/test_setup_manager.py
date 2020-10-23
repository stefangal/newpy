import pytest

@pytest.fixture(scope='session')
def ps():
    from newpy.setup_manger import PrepareSetup
    ps = PrepareSetup()
    return ps

class TestPrepareSetup:


    @pytest.fixture(scope='function')
    def info(self):
        print('\nEnter: gal')

    def test_get_personaldata(self, ps):
        assert isinstance(ps._get_personaldata(), dict)
        assert ps._get_personaldata() == {
            'author': 'StefPy',
            'email': 'stefan.mail.sk@gmail.com',
            'year': '2020'
        }

    def test_item_no_entry(self, ps):
        line = 'name="pkg-YOUR-USERNAME-HERE",'
        assert ps._item(line,
                             "author",
                             "pkg-YOUR-USERNAME-HERE",
                             prefix="pkg-",
                             git=True) == ('pkg-YOUR-USERNAME-HERE',
                                           'pkg-StefPy')

    def test_item_with_entry(self, ps, info):
        line = 'name="pkg-YOUR-USERNAME-HERE",'
        assert ps._item(line,
                             "author",
                             "pkg-YOUR-USERNAME-HERE",
                             prefix="pkg-",
                             git=True) == ('pkg-YOUR-USERNAME-HERE', 'gal')
