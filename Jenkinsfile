pipeline {
    agent any

    stages {
        stage('Clone or Pull') {
            steps {
                script {
                    if (fileExists('dotnet-image-script')) {
                        dir('dotnet-image-script') {
                            sh 'git fetch'
                            sh 'git checkout jenkins/compose.1.0'
                            sh 'git pull origin jenkins/compose.1.0'
                        }
                    } else {
                        sh 'git clone -b jenkins/compose.1.0 https://github.com/Ranur-react/dotnet-image-script.git'
                    }
                }
            }
        }
        stage('Copy .env File') {
            steps {
                script {
                    sh 'cat /mnt/env-aset/dotnet-image-script/sql.env'
                    sh 'cp /mnt/env-aset/dotnet-image-script/sql.env dotnet-image-script/mssql/.env'
                    sh 'cat dotnet-image-script/mssql/.env'
                }
            }
        }
        stage('Container Renewal') {
            steps {
                script {
                    try {
                        sh 'docker stop db_sql1'
                        sh 'docker rm db_sql1'
                    } catch (Exception e) {
                        echo "Container db_sql1 was not running or could not be stopped/removed: ${e}"
                    }
                }
            }
        }
        stage('Delete Image') {
            steps {
                script {
                    try {
                        sh 'docker rmi ranur/mssqlserver:2022'
                    } catch (Exception e) {
                        echo "Image ranur/mssqlserver:2022 could not be removed: ${e}"
                    }
                }
            }
        }
		stage('Renew Image') {
            steps {
				script {
					dir('dotnet-image-script') {
                         dir('mssql') {
                                sh 'docker build -t ranur/mssqlserver:2022 .'
                                }
						
						}
					}
			}
		}
		stage('Build Dockercompose') {
            steps {
				script {
                        dir('dotnet-image-script') {
                            dir('mssql') {
                                // sh 'docker build -t ranur/mssqlserver:2022 .'
                                        sh 'docker-compose up -d'
                                }
                        }
					}

			}
		}
    }
}
