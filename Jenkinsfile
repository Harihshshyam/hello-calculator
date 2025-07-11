pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Harihshshyam/hello-calculator.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install pytest into the workspace-local .local directory
                sh '''
                  python3 -m pip install --upgrade --user pip
                  python3 -m pip install --user -r requirements.txt
                  export PATH="$HOME/.local/bin:$PATH"
                  which pytest  # sanity check
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                  export PATH="$HOME/.local/bin:$PATH"
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
        success { echo '✅ Tests passed and artifacts archived!' }
        failure { echo '❌ Build or Tests failed – see console output.' }
    }
}

