# Kills a process named killmenow

exec { 'pkill -f killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}
