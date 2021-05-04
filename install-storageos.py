import subprocess

if __name__ == '__main__':
    subprocess.run('helm repo add storageos https://charts.storageos.com', shell=True)
    subprocess.run('helm repo update', shell=True)
    subprocess.run('kubectl create namespace storageos', shell=True)
    subprocess.run('helm install storageos storageos/storageos --namespace=storageos --set cluster.join="master01\,worker01\,worker02"', shell=True)
    #subprocess.run('ClusterIP=$(kubectl get svc/storageos --namespace storageos -o custom-columns=IP:spec.clusterIP --no-headers=true)', shell=True)
    #subprocess.run('ApiAddress=$(echo -n "tcp://$ClusterIP:5705" | base64)', shell=True)
    #subprocess.run('kubectl patch secret/storageos-api --namespace storageos --patch \"{\\"data\\": {\\"apiAddress\\": \\"$ApiAddress\\"}}\"', shell=True)
    subprocess.run('kubectl apply -f storageclass.yaml', shell=True)
    subprocess.run('kubectl patch storageclass default -p \'{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}\'', shell=True)
