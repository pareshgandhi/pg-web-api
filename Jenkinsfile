pipeline {
    agent any
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
        stage("Docker push") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh "docker tag pg-web-api:latest pareshgandhi/pg-web-api:latest"
                    sh "docker push pareshgandhi/pg-web-api:latest"
                }
            }
        }
    }
}
