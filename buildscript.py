import subprocess
import time


def build_mln(file):
    print('mln build ' + file + '.mln')
    subprocess.run('mln build -f ' + file + '.mln -r', shell=True)
    print('mln start ' + file)
    subprocess.run('mln start -p ' + file, shell=True)


def check_build(hostname, file):
    build = subprocess.run('nova list --status BUILD | grep ' + hostname, shell=True)
    while build.returncode == 0:
        time.sleep(5)
        print('checking ' + hostname + ' build progress')
        build = subprocess.run('nova list --status BUILD | grep ' + hostname, shell=True)
    print(hostname + ' is done building')

    error = subprocess.run('nova list --status ERROR | grep ' + hostname, shell=True)
    if error.returncode == 0:
        print(hostname + ' had error, trying to rebuild. Please wait.')
        time.sleep(1)
        subprocess.run('nova delete ' + hostname, shell=True)
        print('Deleting ' + hostname)
        time.sleep(10)
        print('Trying to rebuild ' + file)
        build_mln(file)
        check_build(hostname, file)
    else:
        print(hostname + ' was built with no errors')


if __name__ == '__main__':
    # Source .openstack file incase you relogged
    # subprocess.run('source ~/.openstack', shell=True)

    # Master
    print('#--------------------------------BUILDING KUBERNETES MASTER STEP: 1/3--------------------------------#')
    time.sleep(2)
    build_mln('io5-master')
    check_build('kubernetes-master.io5-master', 'io5-master')

    # Worker01
    print('#--------------------------------BUILDING KUBERNETES WORKER01 STEP: 2/3--------------------------------#')
    time.sleep(2)
    build_mln('io5-worker01')
    check_build('kubernetes-worker01.io5-worker01', 'io5-worker01')

    # Worker02
    print('#--------------------------------BUILDING KUBERNETES WORKER02 STEP: 3/3--------------------------------#')
    time.sleep(2)
    build_mln('io5-worker02')
    check_build('kubernetes-worker02.io5-worker02', 'io5-worker02')
