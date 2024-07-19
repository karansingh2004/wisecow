import os
import paramiko
import datetime
import logging

# Set up logging
logging.basicConfig(filename='backup.log', level=logging.INFO)

# Define backup settings
LOCAL_DIR = '/path/to/local/directory'
REMOTE_DIR = '/path/to/remote/directory'
REMOTE_HOST = 'remote_server_ip'
REMOTE_USER = 'remote_server_username'
REMOTE_PASSWORD = 'remote_server_password'

def create_ssh_client():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(REMOTE_HOST, username=REMOTE_USER, password=REMOTE_PASSWORD)
    return ssh

def backup_directory(ssh, local_dir, remote_dir):
    try:
        # Create remote directory if it doesn't exist
        ssh.exec_command(f'mkdir -p {remote_dir}')

        # Backup files using SCP
        scp = ssh.open_sftp()
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(remote_dir, os.path.relpath(local_file, local_dir))
                scp.put(local_file, remote_file)
        scp.close()

        logging.info(f'Backup of {local_dir} to {remote_dir} successful')
        return True
    except Exception as e:
        logging.error(f'Backup failed: {e}')
        return False

def main():
    ssh = create_ssh_client()
    if backup_directory(ssh, LOCAL_DIR, REMOTE_DIR):
        print(f'Backup of {LOCAL_DIR} to {REMOTE_DIR} successful')
    else:
        print(f'Backup of {LOCAL_DIR} to {REMOTE_DIR} failed')
    ssh.close()

if __name__ == '__main__':
    main()