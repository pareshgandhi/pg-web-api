pipeline {
    agent any
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
