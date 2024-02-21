import os
import platform
import psutil  # For retrieving disk usage information

def list_available_drives():
    """List available drives on the system."""
    system = platform.system()
    drives = []
    if system == "Windows":
        drives = [f"{chr(drive)}:\\" for drive in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(drive)}:\\")]
    else:
        drives = [os.path.join(root, entry) for root, _, entries in os.walk('/media') + os.walk('/mnt') + os.walk('/Volumes') for entry in entries]
    return drives

def get_drive_size(drive_path):
    """Get the size of the drive in bytes."""
    usage = psutil.disk_usage(drive_path)
    return usage.total

def select_drive(drives):
    """Prompt the user to select a drive from the available drives."""
    print("Available drives:")
    for i, drive in enumerate(drives, start=1):
        size_gb = get_drive_size(drive) / (1024 ** 3)  # Convert bytes to gigabytes
        print(f"{i}. {drive} ({size_gb:.2f} GB)")
    selection = input("Enter the number corresponding to the drive you want to select: ")
    try:
        selection_index = int(selection) - 1
        if 0 <= selection_index < len(drives):
            return drives[selection_index]
    except ValueError:
        pass
    print("Invalid selection.")
    return None

def secure_delete_and_overwrite_drive(drive_path, overwrite_data):
    """Securely delete and overwrite data on the specified drive."""
    try:
        for root, _, files in os.walk(drive_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, "wb") as f:
                    f.write(overwrite_data)
        print(f"Data securely deleted and overwritten on {drive_path}.")
    except Exception as e:
        print(f"Error occurred while securely deleting and overwriting data on {drive_path}: {e}")

# List available drives and prompt user to select one
drives = list_available_drives()
if drives:
    drive_path = select_drive(drives)
    if drive_path:
        # Get the size of the selected drive
        drive_size = get_drive_size(drive_path)
        
        # Adjust the size of overwrite data based on the size of the drive
        overwrite_data_size_gb = min(drive_size / (1024 ** 3), 1)  # Cap overwrite size at 1 GB
        overwrite_data = os.urandom(int(overwrite_data_size_gb * (1024 ** 3)))  # Convert GB to bytes

        # Perform secure deletion and overwrite on the selected drive
        secure_delete_and_overwrite_drive(drive_path, overwrite_data)
else:
    print("No drives found.")
