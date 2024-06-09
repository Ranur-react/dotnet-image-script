import subprocess

def run_command(command):
    """Run a shell command and print its output."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        print("Error running command: {}".format(command))
        print(result.stderr)
    else:
        print(result.stdout)
    return result

def main():
    commands = [
        "git pull",
        "sudo docker stop net1 || true",  # Ignore error if container does not exist
        "sudo docker rm net1 || true",    # Ignore error if container does not exist
        "sudo docker rmi dotnet1 || true",  # Ignore error if image does not exist
        "sudo docker build -t dotnet1 .",
        "sudo docker run -d -p 8080:8080 --name net1 dotnet1"  # Ensure correct port mapping
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
