# install flask with pip3
class flask {
  package { 'Flask':
    version => '2.1.0',
    ensure    => present,
    provider  => 'pip3',
  }
}
