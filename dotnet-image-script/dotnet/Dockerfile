
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 4001

COPY ./publish .
ENTRYPOINT ["dotnet", "API.dll"]