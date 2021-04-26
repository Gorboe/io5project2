import subprocess

if __name__ == '__main__':
    subprocess.run('kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc6/aio/deploy/recommended.yaml', shell=True)
    subprocess.run('kubectl apply -f kubernetes-dashboard-admin.yaml', shell=True)
