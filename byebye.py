import os
import platform

def list_available_drives():
    """List available drives on the system."""
    system = platform.system()
    drives = []
    if system == "Windows":
        drives = [f"{chr(drive)}:\\" for drive in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(drive)}:\\")]
    elif system == "Linux":
        # On Linux, drives are typically mounted under /media or /mnt
        drives = [os.path.join("/media", entry) for entry in os.listdir("/media") if os.path.isdir(os.path.join("/media", entry))]
        drives += [os.path.join("/mnt", entry) for entry in os.listdir("/mnt") if os.path.isdir(os.path.join("/mnt", entry))]
    elif system == "Darwin":  # macOS
        # On macOS, drives are typically mounted under /Volumes
        drives = [os.path.join("/Volumes", entry) for entry in os.listdir("/Volumes") if os.path.ismount(os.path.join("/Volumes", entry))]
    return drives

def select_drive(drives):
    """Prompt the user to select a drive from the available drives."""
    print("Available drives:")
    for i, drive in enumerate(drives):
        print(f"{i + 1}. {drive}")
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
    for root, dirs, files in os.walk(drive_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, "wb") as f:
                    f.write(overwrite_data)
            except Exception as e:
                print(f"Error: {e}")

# List available drives and prompt user to select one
drives = list_available_drives()
if drives:
    drive_path = select_drive(drives)
    if drive_path:
        # Data to overwrite the files with (e.g., random data)
        overwrite_data = os.urandom(1024)  # Adjust size as needed

        # Perform secure deletion and overwrite on the selected drive
        secure_delete_and_overwrite_drive(drive_path, overwrite_data)
else:
    print("No drives found.")
