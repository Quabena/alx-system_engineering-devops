# A Puppet manifest that kills the process 'killmenow' using the pkill command

exec { 'kill_killmenow':
command => 'pkill killmenow',
path    => '/usr/bin:/bin:/usr/sbin:/sbin',
onlyif  => 'pgrep killmenow',
}
