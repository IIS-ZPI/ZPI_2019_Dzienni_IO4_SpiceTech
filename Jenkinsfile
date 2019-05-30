pipeline {
    agent {
	docker {
		image 'python:3'	
	}
    }
    stages {
        stage('test') {
            steps {
                githubNotify context: 'spajstech-jenkins', credentialsId: 'GitHub', description: 'Jenkins multibranch pipeline running at jenkins.spajstech.ovh',  status: 'PENDING'
                sh 'pip3 install -r requirements.txt'
                sh 'python test/mainTest.py'
                githubNotify context: 'spajstech-jenkins', credentialsId: 'GitHub', description: 'Jenkins multibranch pipeline running at jenkins.spajstech.ovh',  status: 'SUCCESS'
            }
        }
    }
}