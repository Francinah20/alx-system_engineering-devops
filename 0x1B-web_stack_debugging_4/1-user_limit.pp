exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/echo "holberton soft nofile 4096" >> /etc/security/limits.conf && /bin/echo "holberton hard nofile 4096" >> /etc/security/limits.conf && /bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  path    => ['/bin', '/usr/bin'],
  unless  => '/bin/grep -q "holberton soft nofile 4096" /etc/security/limits.conf',
}

