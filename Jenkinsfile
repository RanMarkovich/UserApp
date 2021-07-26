pipeline {
    agent { label 'master' }
    stages{
    stage('checkout'){
     when {
            allOf {
                expression { GIT_BRANCH.startsWith('PR') == false }
                expression { GIT_BRANCH != 'master' }
            }
         }
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