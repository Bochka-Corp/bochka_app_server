pipeline {
    agent any

    stages {
        stage('Build docker image') {
            steps {
                sh '''
                docker-compose build
                '''
            }
        }

        stage('Deploy dev-stand') {
            steps {
                sh '''
                docker compose up -d
                '''
            }
        }
    }
}