# A Puppet manifest to set up my client SSH configuration file

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
