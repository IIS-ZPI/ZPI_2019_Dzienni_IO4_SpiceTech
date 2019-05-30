pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python test/mainTest.py'
            }
        }
    }
}