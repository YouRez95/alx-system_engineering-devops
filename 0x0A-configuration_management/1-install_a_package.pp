# install flask with pip3
class flask {
  python::pip { 'Flask':
    version => '3',
    ensure    => '2.1.0',
    provider  => 'pip3',
  }
}
