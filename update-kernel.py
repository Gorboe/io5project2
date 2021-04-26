import subprocess

if __name__ == '__main__':
    subprocess.run('apt-get update', shell=True)
    subprocess.run('apt install linux-image-4.18.0-25-lowlatency -y', shell=True)
    subprocess.run('update-grub', shell=True)
    subprocess.run('reboot', shell=True)
