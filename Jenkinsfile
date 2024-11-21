pipeline {
    agent any
    stages {
        stage("Test") {
            steps {
                sh """
                /usr/local/bin/docker run hello-world
                """
            }
        }
    }
}
