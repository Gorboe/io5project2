import subprocess
import time

if __name__ == '__main__':
    print('#--------------------------------CREATING NAMESPACE PROJECT2--------------------------------#')
    subprocess.run('kubectl create namespace project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 1/6--------------------------------#')
    print('starting dev-server-1')
    subprocess.run('kubectl apply -f dev-server-1.yaml -n project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 2/6--------------------------------#')
    print('starting dev-server-2')
    subprocess.run('kubectl apply -f dev-server-2.yaml -n project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 3/6--------------------------------#')
    print('starting compile-server-1')
    subprocess.run('kubectl apply -f compile-server-1.yaml -n project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 4/6--------------------------------#')
    print('starting compile-server-2')
    subprocess.run('kubectl apply -f compile-server-2.yaml -n project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 5/6--------------------------------#')
    print('starting storage-server-1')
    subprocess.run('kubectl apply -f storage-server-1.yaml -n project2', shell=True)
    time.sleep(1)

    print('#--------------------------------BUILDING PODS STEP: 6/6--------------------------------#')
    print('starting storage-server-2')
    subprocess.run('kubectl apply -f storage-server-2.yaml -n project2', shell=True)
    time.sleep(10)

    print('Installing required packages to containers')
    time.sleep(5)
    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get update', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get update', shell=True)
    subprocess.run('kubectl exec compile-server-1 -n project2 -- apt-get update', shell=True)
    subprocess.run('kubectl exec compile-server-2 -n project2 -- apt-get update', shell=True)
    subprocess.run('kubectl exec storage-server-1 -n project2 -- apt-get update', shell=True)
    subprocess.run('kubectl exec storage-server-2 -n project2 -- apt-get update', shell=True)

    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)
    subprocess.run('kubectl exec compile-server-1 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)
    subprocess.run('kubectl exec compile-server-2 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)
    subprocess.run('kubectl exec storage-server-1 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)
    subprocess.run('kubectl exec storage-server-2 -n project2 -- apt-get install -y puppet augeas-tools', shell=True)

    subprocess.run('kubectl cp users.pp project2/dev-server-1:/', shell=True)
    subprocess.run('kubectl cp users.pp project2/dev-server-2:/', shell=True)
    subprocess.run('kubectl cp users.pp project2/compile-server-1:/', shell=True)
    subprocess.run('kubectl cp users.pp project2/compile-server-2:/', shell=True)
    subprocess.run('kubectl cp users.pp project2/storage-server-1:/', shell=True)
    subprocess.run('kubectl cp users.pp project2/storage-server-2:/', shell=True)

    subprocess.run('kubectl exec dev-server-1 -n project2 -- puppet apply users.pp', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- puppet apply users.pp', shell=True)
    subprocess.run('kubectl exec compile-server-1 -n project2 -- puppet apply users.pp', shell=True)
    subprocess.run('kubectl exec compile-server-2 -n project2 -- puppet apply users.pp', shell=True)
    subprocess.run('kubectl exec storage-server-1 -n project2 -- puppet apply users.pp', shell=True)
    subprocess.run('kubectl exec storage-server-2 -n project2 -- puppet apply users.pp', shell=True)

    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get install emacs -y', shell=True)
    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get install jed -y', shell=True)
    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get install subversion -y', shell=True)
    subprocess.run('kubectl exec dev-server-1 -n project2 -- apt-get install git -y', shell=True)

    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get install emacs -y', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get install jed -y', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get install subversion -y', shell=True)
    subprocess.run('kubectl exec dev-server-2 -n project2 -- apt-get install git -y', shell=True)

    subprocess.run('kubectl exec compile-server-1 -n project2 -- apt-get install gcc -y', shell=True)
    subprocess.run('kubectl exec compile-server-1 -n project2 -- apt-get install make', shell=True)
    subprocess.run('kubectl exec compile-server-1 -n project2 -- apt-get install binutils', shell=True)

    subprocess.run('kubectl exec compile-server-2 -n project2 -- apt-get install gcc -y', shell=True)
    subprocess.run('kubectl exec compile-server-2 -n project2 -- apt-get install make', shell=True)
    subprocess.run('kubectl exec compile-server-2 -n project2 -- apt-get install binutils', shell=True)

    subprocess.run('kubectl exec storage-server-1 -n project2 -- apt install glusterfs-server -y', shell=True)

    subprocess.run('kubectl exec storage-server-2 -n project2 -- apt install glusterfs-server -y', shell=True)

    print('Installation completed')
