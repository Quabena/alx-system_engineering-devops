# This Puppet manifest installs a specific version of flask (2.1.0) using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

