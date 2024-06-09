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
        "docker stop sql1",
        "docker rm sql1",
        "docker rmi mssqlserver",
        "docker build -t mssqlserver .",
        "docker run -d --name sql1 -p 1433:1433 mssqlserver"
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
