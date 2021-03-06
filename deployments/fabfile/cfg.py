"""
Define generic constants for reusabililty
"""

from os.path import join, sep

from fabric.api import env

env.HOME_DIR = join(sep, 'opt')
env.REPO_DIR = join(env.HOME_DIR, 'grmp')
env.REPO_URL = 'git@github.com:judeconnectionz/grmp.git'
env.OPS_DIR = join(env.REPO_DIR, 'deployments')
env.OPS_ETC_DIR = join(env.OPS_DIR, 'ubuntu', 'etc')

# add subdomains to this list separated with a comma
env.DOMAINS = 'grmp.serthe.com'