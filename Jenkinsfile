pipeline {
    agent { dockerfile true }
    stages {
        stage("Test") {
            steps {
                sh """
                docker run hello-world
                """
            }
        }
    }
}
