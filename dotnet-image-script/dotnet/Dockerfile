
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
# COPY  /sources .
# ENTRYPOINT ["dotnet", "API.dll"]


FROM base AS final
WORKDIR /app
COPY --from=build /sources .
ENTRYPOINT ["dotnet", "API.dll"]