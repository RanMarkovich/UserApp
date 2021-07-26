pipeline {
    agent { label 'master' }
    stages{
        stage('checkout'){
            steps {checkout scm}
        }
        stage('build'){
            steps {sh '''docker-compose up -d --build '''}
        }
        stage('teardown'){
           steps { sh '''docker-compose down '''}
        }
  }
}