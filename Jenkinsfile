pipeline {
    agent { label 'master' }
    stages{
        stage('build'){
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
            agent { docker { image 'python:3.9' } }
            steps {
                sh '''python -m pip install --user tests/requirements.txt'''
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
