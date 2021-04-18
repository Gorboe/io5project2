group { 'developers':
    ensure => present,
}

user { 'bob':
    ensure => present,
    groups => ['sudo'],
    home => '/home/bob',
    managehome => true,
    password => '$1$t8DZHbJJ$1utDkUuhNDV2bufgusNlN/',
}

user { 'janet':
    ensure => present,
    groups => ['sudo', 'developers'],
    managehome => true,
    home => '/home/janet',
    password => '$1$i9/WigkY$d8qdnMxd9ZcFsmcr7i1vr0',
}

user { 'alice':
    ensure => present,
    groups => ['sudo'],
    managehome => true,
    password => '$1$D7txi.o1$9kedAf.249apnFiOUbhiZ1',
}

user { 'tim':
    ensure => present,
    groups => ['sudo', 'developers'],
    managehome => true,
    password => '$1$6om/ecf.$01qXloLHVudhwvpCdO2Jb1',
}
