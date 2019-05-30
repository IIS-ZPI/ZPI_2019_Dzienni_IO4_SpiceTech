pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                git branch: 'feature/jenkins-ci', credentialsId: 'GitHub', url: 'https://github.com/IIS-ZPI/ZPI_2019_Dzienni_IO4_SpiceTech'
                githubNotify context: 'jenkins', description: 'Jenkins multibranch pipeline',  status: 'PENDING'
                sh 'echo No tests at the moment, exiting.'
                githubNotify context: 'jenkins', description: 'Jenkins multibranch pipeline',  status: 'SUCCESS'
            }
        }
    }
}