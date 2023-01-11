#Installs a package

package { 'flask':
ensure   => 'present',
provider => 'pip3',
}
