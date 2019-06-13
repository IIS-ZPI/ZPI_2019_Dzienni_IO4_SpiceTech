pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 test/mainTest.py'
                sh 'echo Checking coverage...'
                sh 'pip3 install coverage'
                sh 'coverage run --source src test/mainTest.py'
                sh 'coverage report -m'
            }
        }
    }
}