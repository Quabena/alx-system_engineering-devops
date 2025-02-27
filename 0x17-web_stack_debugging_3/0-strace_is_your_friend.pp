# This Puppet manifest fixes missing PHP modules and restarts Apache

class { 'apache':
  service_ensure => 'running',
}

package { ['php5', 'libapache2-mod-php5', 'php5-mysql']:
  ensure => installed,
}

exec { 'restart-apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => Package['php5'],
}

file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}
