pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/gopikasivakumar07-crypto/greatestofthree.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Greatest of Three Numbers application...'
                bat 'python -m py_compile greatest.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'python -m pytest test_greatest.py'
            }
        }
    }
}