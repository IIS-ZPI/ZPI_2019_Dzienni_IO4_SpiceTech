pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'cd test; python3 mainTest.py'
                sh 'echo Checking coverage...'
                sh 'pip3 install coverage'
                sh 'coverage run test/mainTest.py'
                sh 'coverage report -m'
            }
        }
    }
}