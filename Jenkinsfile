pipeline {
    agent any
    environment {
      PATH = "/usr/local/bin:${env.PATH}"
    }
    stages {
        stage("Test") {
            steps {
                sh """
                docker compose build
                """
            }
        }
    }
}
