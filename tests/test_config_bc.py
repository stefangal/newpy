import pytest
from newpy.config_bc import ConfigBuildCheck


class TestConfigBuildCheck:
    @pytest.fixture(scope='class')
    def cbcIn(self):
        cbc = ConfigBuildCheck()
        return cbc

    def test_test(self, cbcIn):
        assert True

    def test_new_config_file(self, cbcIn):
        assert cbcIn.proba() == 4
