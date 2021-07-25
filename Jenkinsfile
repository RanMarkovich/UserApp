pipeline {
    agent { label 'master' }
    stages{
//     stage('checkout'){
//         steps {checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'b6b2c45b-ebaf-4913-aed4-c6081b0efe97', url: 'https://github.com/RanMarkovich/UserApp.git']]])}
//     }
    stage('build'){
        steps {sh '''docker-compose up -d --build '''}
    }
    stage('teardown'){
       steps { sh '''docker-compose down '''}
    }
  }
}
//////