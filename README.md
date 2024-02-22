# ByeBye

**ByeBye** is a Python script designed to securely delete and overwrite data on drives in a system. It provides a simple interface for users to select a drive and securely erase its contents, making the data unrecoverable.

## Features

- **OS Detection**: Detects the operating system and lists available drives accordingly.
- **Drive Selection**: Allows the user to select a drive from the list of available drives.
- **Secure Deletion**: Overwrites data on the selected drive multiple times with random data, making it virtually impossible to recover.
- **Feedback**: Provides informative messages to guide users through the process and handle errors gracefully.

## Requirements

- Python 3.x
- Supported operating systems: Windows, Linux, macOS

## Usage

### Running the Script Locally

1. **Clone the Repository**: Clone or download the ByeBye repository to your local machine.
```bash
https://github.com/confox/ByeBye
```

2. **Navigate to the Script**: Open a terminal or command prompt and navigate to the directory containing the `byebye.py` script.

3. **Run the Script**: Execute the script using the Python interpreter:

    ```bash
    python byebye.py
    ```

4. **Follow the Prompts**: Select a drive from the list of available drives and confirm to securely delete its contents.

    **Note:** Ensure you have necessary permissions and backups before proceeding.

### Running the Script Remotely

1. **Set Up Remote Machine**: Ensure that your remote machine (e.g., a VirtualBox VM) is configured with a network adapter that allows network connectivity.

2. **Install SSH Server**: If not already installed, install and configure an SSH server on the remote machine.

3. **Determine IP Address**: Obtain the IP address of the remote machine.

4. **SSH Connection**: From your local machine's terminal or command prompt, initiate an SSH connection:

    ```bash
    ssh username@remote_host 'python /path/to/your/script.py'
    ```

    Replace `username` with your remote machine's username, `remote_host` with its hostname or IP address, and `/path/to/your/script.py` with the path to your Python script.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
