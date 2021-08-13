pipeline {
    agent { label 'master'}
    stages{
        stage('build'){
            steps {
                sh '''docker-compose up -d --build'''
            }
        }
        stage('test'){
            agent {
                        docker {
                            image 'qnib/pytest'
                            reuseNode true
                            args "--network my-network"
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
//             junit 'reports/*.xml '
            sh '''docker-compose down'''
            sh '''docker system prune -af'''
            sh '''docker volume prune -f'''
        }
    }
}