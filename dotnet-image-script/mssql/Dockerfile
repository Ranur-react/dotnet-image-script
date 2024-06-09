# Menggunakan image dasar SQL Server 2022
FROM mcr.microsoft.com/mssql/server:2022-latest

# Menetapkan variabel environment untuk menerima EULA dan password SA
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=12345678

# Membuka port 1433
EXPOSE 1433

# Menentukan perintah untuk menjalankan SQL Server ketika container dimulai
CMD /opt/mssql/bin/sqlservr
