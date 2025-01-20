# 2-puppet_custom_http_response_header.pp

# Ensure that nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create a custom Nginx configuration with the X-Served-By header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/custom_header.conf.erb'),
  notify  => Service['nginx'],  # Notify Nginx to reload after changes
}

# Ensure that the nginx configuration is valid
exec { 'nginx_test':
  command => '/usr/sbin/nginx -t',
  path    => ['/usr/sbin', '/usr/bin'],
  onlyif  => '/usr/sbin/nginx -t',
  require => File['/etc/nginx/sites-available/default'],
}

# Reload Nginx if configuration is correct
service { 'nginx_reload':
  ensure      => 'running',
  name        => 'nginx',
  subscribe   => Exec['nginx_test'],  # Reload on successful configuration test
  refreshonly => true,
}

