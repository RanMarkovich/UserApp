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
            agent {
                        docker {
                            image 'qnib/pytest'
                            reuseNode true
                            args "--network ${env.NETWORK_ID}"
                            }
                       }
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
