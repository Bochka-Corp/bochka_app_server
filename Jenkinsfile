pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Здесь могут быть инструкции по сборке вашего проекта, например:
                // sh 'make'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the project...'
                // Здесь могут быть инструкции по тестированию вашего проекта, например:
                // sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                // Здесь могут быть инструкции по деплою вашего проекта на виртуальной машине, например:
                // sh 'make deploy'
            }
        }
    }
}