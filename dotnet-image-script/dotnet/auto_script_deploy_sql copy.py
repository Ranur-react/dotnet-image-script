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
        "docker stop net1",
        "docker rm net1",
        "docker rmi dotnet1",
        "docker build -t dotnet1 .",
        "docker run -d --name net1  -p 4001:80 dotnet1"
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
