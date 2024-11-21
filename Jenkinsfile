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
        stage("Docker push") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh "docker push pareshgandhi/webapi:pg-web-api:latest"
                }
            }
        }
    }
}
