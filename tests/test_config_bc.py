import pytest
from ..newpy.config_bc import ConfigBuildCheck


class TestConfigBuildCheck:

    @pytest.fixture(scope='module')
    def setup(self):
        print("--------- setup running ---------")       

    def test_new_config_file(self, setup):
        assert ConfigBuildCheck().check_options_ok()