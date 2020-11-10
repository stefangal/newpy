# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

import pytest
import mock
import builtins


@pytest.fixture(scope='session')
def ps():

    from newpy.setup_manager import PrepareSetup

    ps = PrepareSetup()
    return ps


class TestPrepareSetup:
    """
    Testing the setup_manager
    """
    @pytest.skip("only for local test")
    def test_get_personaldata_local(self, ps):
        assert isinstance(ps._get_personaldata(), dict)
        assert ps._get_personaldata() == {
            'author': 'StefPy',
            'email': 'stefan.mail.sk@gmail.com',
            'year': '2020'
        }

    def test_get_personaldata(self, ps):
        assert isinstance(ps._get_personaldata(), dict)
        assert ps._get_personaldata() == {
            'author': 'Travis CI User',
            'email': 'travis@example.org',
            'year': '2020'
        }

    @pytest.skip("only for local test")
    def test_item_no_entry_local(self, ps):
        with mock.patch.object(builtins, 'input', lambda _: mock.call):
            line = 'name="pkg-YOUR-USERNAME-HERE",'
            assert ps._item(line,
                            "author",
                            "pkg-YOUR-USERNAME-HERE",
                            prefix="pkg-",
                            git=True) == ('pkg-YOUR-USERNAME-HERE',
                                          'pkg-StefPy')

    def test_item_no_entry(self, ps):
        with mock.patch.object(builtins, 'input', lambda _: mock.call):
            line = 'name="pkg-YOUR-USERNAME-HERE",'
            assert ps._item(line,
                            "author",
                            "pkg-YOUR-USERNAME-HERE",
                            prefix="pkg-",
                            git=True) == ('pkg-YOUR-USERNAME-HERE',
                                          'pkg-Travis CI User')

    def test_item_with_entry(self, ps):
        with mock.patch.object(builtins, 'input', lambda _: 'gal'):
            line = 'name="pkg-YOUR-USERNAME-HERE",'
            output = ps._item(line,
                              "author",
                              "pkg-YOUR-USERNAME-HERE",
                              prefix="pkg-",
                              git=True)
            assert output == ('pkg-YOUR-USERNAME-HERE', 'gal')