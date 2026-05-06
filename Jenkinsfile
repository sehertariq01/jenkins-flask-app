pipeline {
    agent any

    stages {

        stage('Code Linting') {
            steps {
                sh 'pip install flake8 --break-system-packages'
                sh '/var/lib/jenkins/.local/bin/flake8 .'
            }
        }

        stage('Code Build') {
            steps {
               sh 'docker build --no-cache -t flask-app .'
            }
        }

        stage('Containerized Deployment') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                sh 'docker build -t selenium-tests ./tests'
                sh 'docker run --network host selenium-tests'
            }
        }
    }
}