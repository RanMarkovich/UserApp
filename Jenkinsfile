pipeline {
    agent { label 'master'}
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
            agent { docker { reuseNode true image 'ranmarkovich/agent-jenkins-docker-python'} }
            steps {
                sh '''pip install requests'''
                sh '''pytest tests/user_app_tests/test_ping.py'''
            }
        }
      }
      post {
        always {
            sh '''docker-compose down'''
            sh '''docker rm -f $(docker ps -a -q)'''
        }
    }
}//
