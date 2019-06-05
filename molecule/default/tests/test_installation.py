"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """
    Ensure /etc/iptables/rules.v4 file exists
    """

    f = host.file('/etc/iptables/rules.v4')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_iptables_rules(host):
    """
    Ensure /etc/iptables/rules.v4 is applied
    """
    r = host.iptables.rules(chain='INPUT')
    print r
    assert "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT" in r
