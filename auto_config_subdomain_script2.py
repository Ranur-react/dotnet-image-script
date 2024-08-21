import subprocess
import os
from datetime import datetime

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.returncode != 0:
            print("Error running command: {}".format(command))
            print(result.stderr)
        else:
            print(result.stdout)
    except Exception as e:
        print("Exception running command: {}".format(command))
        print(e)

def backup_apache_config():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#    backup_dir = f"/etc/apache2/backup_{timestamp}"
    backup_dir = "/etc/apache2/backup_{}".format(timestamp)
    os.makedirs(backup_dir, exist_ok=True)
    run_command("cp -r /etc/apache2/sites-available".format(backup_dir))
    run_command("cp -r /etc/apache2/sites-enabled".format(backup_dir))
    run_command("cp /etc/apache2/apache2.conf".format(backup_dir))
    run_command("cp /etc/apache2/ports.conf".format(backup_dir))
    print("Backup of Apache configuration is saved")

def install_certbot():
    print("Installing Certbot and Apache plugin...")
    run_command("apt update")
    run_command("apt install -y certbot python3-certbot-apache")

def create_apache_config():
    config = """
<VirtualHost *:80>
    ServerName squareapi.numpang.my.id

    ProxyPreserveHost On
    ProxyPass / http://114.7.96.242:4001/
    ProxyPassReverse / http://114.7.96.242:4001/

    ErrorLog ${APACHE_LOG_DIR}/squareapi_error.log
    CustomLog ${APACHE_LOG_DIR}/squareapi_access.log combined
</VirtualHost>
"""
    with open('/etc/apache2/sites-available/squareapi.numpang.my.id.conf', 'w') as f:
        f.write(config)
    print("Apache configuration file created for squareapi.numpang.my.id")

def enable_site_and_reload():
    run_command("a2ensite squareapi.numpang.my.id.conf")
    run_command("systemctl reload apache2")

def obtain_ssl_certificate():
    print("Obtaining SSL certificate for domain: squareapi.numpang.my.id...")
    run_command("certbot --apache -d squareapi.numpang.my.id --non-interactive --agree-tos --email your-email@example.com")
    print("SSL certificate obtained for squareapi.numpang.my.id")

def main():
    backup_apache_config()
    install_certbot()
    create_apache_config()
    enable_site_and_reload()
    obtain_ssl_certificate()
    run_command("systemctl reload apache2")
    print("Configuration for squareapi.numpang.my.id has been successfully applied.")

if __name__ == "__main__":
    main()

