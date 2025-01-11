# This Puppet manifest installs Flask version 2.1.0 and ensures compatibility with Werkzeug

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.2',
  path    => '/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

