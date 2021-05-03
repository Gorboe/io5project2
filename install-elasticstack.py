import subprocess

if __name__ == '__main__':
    subprocess.run('helm repo add elastic https://helm.elastic.co', shell=True)
    subprocess.run('helm repo update', shell=True)
    subprocess.run('kubectl create namespace logging', shell=True)
    subprocess.run('helm install elasticsearch elastic/elasticsearch -n logging', shell=True)
    subprocess.run('helm install kibana elastic/kibana -n logging', shell=True)
    subprocess.run('helm install metricbeat elastic/metricbeat -n logging', shell=True)
    subprocess.run('helm install filebeat elastic/filebeat -n logging', shell=True)
