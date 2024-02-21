# ByeBye

ByeBye is a Python script designed to securely delete and overwrite data on drives in a system. It provides a simple interface for users to select a drive and securely erase its contents, making the data unrecoverable.

## Features

- Detects the operating system and lists available drives accordingly.
- Allows the user to select a drive from the list of available drives.
- Securely deletes and overwrites data on the selected drive, making it unrecoverable.
- Provides feedback and error messages to the user during the process.

## Requirements

- Python 3.x
- Operating system: Windows, Linux, macOS

## Usage

### Running the Script Locally

1. Clone or download the ByeBye repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `byebye.py` script.
4. Run the script using the Python interpreter:

    ```
    python byebye.py
    ```

5. Follow the prompts to select a drive and securely delete its contents.

**Note:** Ensure that you have appropriate permissions to modify the files on the selected drive. Always make sure you have backups of important data before running the script.

### Running the Script Remotely

1. Ensure that your remote machine (e.g., a VirtualBox VM) is configured with a network adapter that allows network connectivity.
2. Install and configure an SSH server on the remote machine if not already installed.
3. Determine the IP address of the remote machine.
4. From your local machine, open a terminal or command prompt.
5. Use the `ssh` command to connect to the remote machine and execute the script remotely:

    ```bash
    ssh username@remote_host 'python /path/to/your/script.py'
    ```

    Replace `username` with your username on the remote machine, `remote_host` with the hostname or IP address of the remote machine, and `/path/to/your/script.py` with the path to your Python script on the remote machine.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
