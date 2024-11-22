pipeline {
    agent {label 'jenkins_agent' }
    environment {
      PATH = "/usr/local/bin:${env.PATH}"
    }
    stages {
        stage("Docker build") {
            steps {
                sh """
                docker compose build
                """
            }
        }
        stage("Test the built image") {
            steps {
                sh "docker run pg-web-api:latest pytest tests/"
            }
        }
    }
}

