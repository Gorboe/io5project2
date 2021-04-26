import subprocess
import sys

if __name__ == '__main__':
    subprocess.run('apt-get update', shell=True)
    subprocess.run('apt-get install ebtables arptables -y', shell=True)
    subprocess.run('echo "net.bridge.bridge-nf-call-ip6tables = 1" >> /etc/sysctl.d/k8s.conf', shell=True)
    subprocess.run('echo "net.bridge.bridge-nf-call-iptables = 1" >> /etc/sysctl.d/k8s.conf', shell=True)
    subprocess.run('sysctl --system', shell=True)
    subprocess.run('modprobe br_netfilter', shell=True)
    subprocess.run('swapoff -a', shell=True)
    subprocess.run('apt-get update', shell=True)
    subprocess.run('apt install docker.io -y', shell=True)
    subprocess.run('apt-get update', shell=True)
    subprocess.run('curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add', shell=True)
    subprocess.run('apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"', shell=True)
    subprocess.run('apt-get update', shell=True)
    subprocess.run('apt-get install -y kubelet kubeadm kubectl', shell=True)
    subprocess.run('apt-mark hold kubeadm kubelet kubectl', shell=True)
    subprocess.run('hostnamectl set-hostname ' + str(sys.argv[0]), shell=True)
