import subprocess

if __name__ == '__main__':
    subprocess.run('apt-get update', shell=True)
    subprocess.run('curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -', shell=True)
    subprocess.run('sudo apt-get install apt-transport-https --yes', shell=True)
    subprocess.run('echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list', shell=True)
    subprocess.run('apt-get update', shell=True)
    subprocess.run('apt-get install helm', shell=True)
