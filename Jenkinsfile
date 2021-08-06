pipeline {
    agent { label 'master'  reuseNode true }
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
            agent { docker { image 'qnib/pytest'} }
            steps {
                sh '''pip install requests'''
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
