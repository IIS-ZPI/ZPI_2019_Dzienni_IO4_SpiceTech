pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python test/mainTest.py'
		sh 'echo Checking coverage...'
		sh 'pip3 install coverage'
		sh 'coverage run test/maintest.py'
		sh 'coverage report -m'
            }
        }
    }
}