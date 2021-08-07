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
                            args "--network user_app_multibranch_${BRANCH_NAME}_my_network"
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
            sh '''docker system prune -af'''
            sh '''docker volume prune -f'''
        }
    }
}