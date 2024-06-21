pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/bjesuslopezg/python-ci-test'
            }
        }

        stage('List Files') {
            steps {
                sh 'ls -al'
            }
        }

        stage('Build Project') {
            agent {
                docker {
                    image 'python:3.7.2'
                    args '-u root -v $WORKSPACE:$WORKSPACE -w $WORKSPACE'
                }
            }
            steps {
                sh 'ls -al'
                sh 'cat requirements.txt'

                // Setup virtual environment and install dependencies
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                
                // Build project (example: package the application)
                sh '. venv/bin/activate && python setup.py sdist'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
