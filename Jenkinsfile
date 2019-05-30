pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                git branch: 'feature/jenkins-ci', credentialsId: 'GitHub', url: 'https://github.com/IIS-ZPI/ZPI_2019_Dzienni_IO4_SpiceTech'
                githubNotify context: 'spajstech-jenkins', description: 'Jenkins multibranch pipeline running at jenkins.spajstech.ovh',  status: 'PENDING'
                sh 'pip3 install -r requirements'
                sh 'python test/mainTest.py'
                githubNotify context: 'spajstech-jenkins', description: 'Jenkins multibranch pipeline running at jenkins.spajstech.ovh',  status: 'SUCCESS'
            }
        }
    }
}