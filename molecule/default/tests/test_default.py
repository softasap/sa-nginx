import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_installed(host):
    nginx = host.package('nginx')

    assert nginx.is_installed


def test_nginx_service(host):
    nginx = host.service('nginx')

    assert nginx.is_enabled


def test_nginx_sites_layout(host):
    assert host.file('/etc/nginx/sites-available').is_directory
    assert host.file('/etc/nginx/sites-enabled').is_directory
    assert host.file('/etc/nginx/snippets').is_directory
