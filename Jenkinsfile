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
        stage('Install Dependencies') {
            steps {
                sh '''
                  pip install --upgrade pip pytest
                  pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
            post { always { junit 'results.xml' } }
        }
        stage('Archive Sources') {
            steps {
                archiveArtifacts artifacts: 'app.py, test_app.py, requirements.txt', fingerprint: true
            }
        }
    }

    post {
        success { echo '✅ Tests passed and artifacts archived!' }
        failure { echo '❌ कुछ फेल हुआ—लॉग देखें।' }
    }
}
