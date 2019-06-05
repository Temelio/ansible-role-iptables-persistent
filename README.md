# iptables-persistent

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/Temelio/ansible-role-iptables-persistent.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-iptables-persistent)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-iptables-persistent/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-statsd/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-iptables-persistent/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-statsd/)
[![Ansible Role](https://img.shields.io/ansible/role/.svg)](https://galaxy.ansible.com/Temelio/statsd/)
[![GitHub tag](https://img.shields.io/github/tag/Temelio/ansible-role-iptables-persistent.svg)](https://github.com/Temelio/ansible-role-iptables-persistent/tags)

Install iptables-persistent package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Stretch
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: temelio.iptables-persistent }
```

## License

MIT

## Author Information

Lise Machetel (for Temelio company)
- https://temelio.com
- lise.machetel [at] temelio.com
