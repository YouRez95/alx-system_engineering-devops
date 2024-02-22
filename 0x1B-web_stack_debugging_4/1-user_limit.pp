# user limit

file { 'user limit':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  content => ''
}
