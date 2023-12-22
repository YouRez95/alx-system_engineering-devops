# install flask with pip3

package { 'flask':
  version   => '2.1.0',
  provider  => 'pip3',
  ensure    => installed,
}
