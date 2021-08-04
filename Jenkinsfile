pipeline {
    agent none
    stages{
        stage('build'){
            agent { label 'master' }
            steps {
            script {
                try {
                    sh '''docker-compose up -d --build '''
                } catch (err) {
                    echo err.getMessage()
               }
             }
           }
        }
        stage('test'){
            agent { docker { image 'python:3.9-alpine' } }
            steps {
                sh '''sudo pip3 install -r tests/requirements.txt --user'''
                sh '''pytest tests/user_app_tests/test_ping.py'''
            }
        }
      }
      post {
        always {
            sh '''docker-compose down'''
        }
    }
}//
