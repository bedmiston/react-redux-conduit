from fabric.api import env, local, settings, abort, run, cd


def v():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
    # Set the site path
    env.vagrant_folder = '/vagrant/'
    env.site_path = '/vagrant/conduit/'

    # use vagrant ssh key
    result = local(
        'vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


def host_type():
    run('uname -s')


def start():
    """Run node server."""
    with cd(env.site_path):
        run('npm start')
