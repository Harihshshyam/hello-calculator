pipeline {
    agent {
        docker {
            image 'python:3.9'
            args  '-u root:root'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Harihshshyam/hello-calculator.git', branch: 'main'
            }
        }
        stage('Install pip & Dependencies') {
            steps {
                sh '''
                  apt-get update && apt-get install -y python3-pip
                  pip3 install --upgrade pip
                  pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveA
