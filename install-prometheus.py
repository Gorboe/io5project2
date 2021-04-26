import subprocess

if __name__ == '__main__':
    subprocess.run('helm repo add stable https://charts.helm.sh/stable', shell=True)
    subprocess.run('helm repo update', shell=True)
    subprocess.run('kubectl create namespace monitoring', shell=True)
    subprocess.run('helm install my-prometheus-operator stable/prometheus-operator --namespace=monitoring', shell=True)
