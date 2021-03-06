import sys
import mock

charmhelpers = None
apt_pkg = None


def mock_charmhelpers():
    # Mock out charmhelpers so that we can test without it.
    # also stops sideeffects from occuring.
    global charmhelpers
    global apt_pkg
    charmhelpers = mock.MagicMock()
    apt_pkg = mock.MagicMock()
    sys.modules['apt_pkg'] = apt_pkg
    sys.modules['charmhelpers'] = charmhelpers
    sys.modules['charmhelpers.core'] = charmhelpers.core
    sys.modules['charmhelpers.core.hookenv'] = charmhelpers.core.hookenv
    sys.modules['charmhelpers.core.host'] = charmhelpers.core.host
    sys.modules['charmhelpers.core.unitdata'] = charmhelpers.core.unitdata
    sys.modules['charmhelpers.core.templating'] = charmhelpers.core.templating
    sys.modules['charmhelpers.contrib'] = charmhelpers.contrib
    sys.modules['charmhelpers.contrib.openstack'] = (
        charmhelpers.contrib.openstack)
    sys.modules['charmhelpers.contrib.openstack.context'] = (
        charmhelpers.contrib.openstack.context)
    sys.modules['charmhelpers.contrib.openstack.ha'] = (
        charmhelpers.contrib.openstack.ha)
    sys.modules['charmhelpers.contrib.openstack.ha.utils'] = (
        charmhelpers.contrib.openstack.ha.utils)
    sys.modules['charmhelpers.contrib.openstack.utils'] = (
        charmhelpers.contrib.openstack.utils)
    sys.modules['charmhelpers.contrib.openstack.cert_utils'] = (
        charmhelpers.contrib.openstack.cert_utils)
    sys.modules['charmhelpers.contrib.openstack.templating'] = (
        charmhelpers.contrib.openstack.templating)
    sys.modules['charmhelpers.contrib.network'] = charmhelpers.contrib.network
    sys.modules['charmhelpers.contrib.network.ip'] = (
        charmhelpers.contrib.network.ip)
    sys.modules['charmhelpers.fetch'] = charmhelpers.fetch
    sys.modules['charmhelpers.cli'] = charmhelpers.cli
    sys.modules['charmhelpers.contrib.hahelpers'] = (
        charmhelpers.contrib.hahelpers)
    sys.modules['charmhelpers.contrib.hahelpers.cluster'] = (
        charmhelpers.contrib.hahelpers.cluster)
    sys.modules['charmhelpers.core.hookenv.charm_dir'] = (
        charmhelpers.core.hookenv.charm_dir)
    charmhelpers.core.hookenv.charm_dir.return_value = "/tmp"

    # mock in the openstack releases so that the tests can run
    charmhelpers.contrib.openstack.utils.OPENSTACK_RELEASES = (
        'diablo',
        'essex',
        'folsom',
        'grizzly',
        'havana',
        'icehouse',
        'juno',
        'kilo',
        'liberty',
        'mitaka',
        'newton',
        'ocata',
        'pike',
        'queens',
        'rocky',
    )
