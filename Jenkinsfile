pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                python -m venv .venv
                source .venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start FastAPI server') {
            steps {
                sh '''
                source .venv/bin/activate
                uvicorn main:app --host 0.0.0.0 --port 8000 --reload
                '''
            }
        }
    }
}