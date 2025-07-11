pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Harihshshyam/hello-calculator.git', branch: 'main'
            }
        }

        stage('Setup & Install') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                  . venv/bin/activate
                  pytest --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'app.py, test_app.py, requirements.txt', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ All tests passed and artifacts archived!'
        }
        failure {
            echo '❌ Something failed, check logs!'
        }
    }
}

