pipeline {
    agent any

    stages {

        stage('Code Linting') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }

        stage('Code Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Containerized Deployment') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }
    }
}