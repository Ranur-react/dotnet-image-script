# Deploym the .NET Core  project with Docker

Panduan ini menjelaskan langkah-langkah untuk mempublikasikan proyek .NET Core API Anda dan menjalankannya dalam container Docker.

## Langkah 1: Publish Proyek ke Folder

Jalankan perintah berikut untuk mempublikasikan proyek Anda ke folder tertentu:

```sh
dotnet publish -c Release -o C:\Users\rahma\OneDrive\Documents\docker-developer\dotnet-image-script\dotnet/publish

```

## Langkah 2: Konfigurasi Dockerfile seperti berikut

```Dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 4001

COPY ./publish .
ENTRYPOINT ["dotnet", "API.dll"]

```

## Langkah 3: Konfigurasi Aplikasi ASP.NET Core


Tambahkan app.Urls.Add("http://*:4001"); ke dalam Program.cs:

```csharp
var builder = WebApplication.CreateBuilder(args);

// Additional code here...

var app = builder.Build();

app.Urls.Add("http://*:4001"); // Ensure the application listens on the correct port

app.Run();

```

## Langkah 4: Skrip Python untuk Build dan Deploy

```python
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
        "sudo docker run -d -p 4001:4001 --name net1 dotnet1"  # Ensure correct port mapping
    ]

    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()


```

## Langkah 5: Jalankan scrip pyrthon

```sh
sudo python3 auto_script_deploy_net.py
```


## Langkah 6: Pastikan Firewall pada server Mengizinkan Port
Pastikan port 4001 terbuka di firewall:

```sh
sudo ufw allow 4001
```
Dengan langkah-langkah ini, aplikasi Anda sekarang seharusnya dapat diakses API di <http://ip:4001/> via POSTMAN atau script kodingan anda. Jika ada masalah lebih lanjut atau pertanyaan tambahan, jangan ragu untuk bertanya kepada saya secara pribadi lewat linkedin atau email rahmatnur844@gmail.com.

