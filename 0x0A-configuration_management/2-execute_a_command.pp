# kill a process named killmenow

exec { 'pkill -f killmenow':
  path => '/usr/bin',
}
