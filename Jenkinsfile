pipeline {
    agent { label 'master'}
    stages{
        stage('Preparing Test Environment'){
            steps {
                sh '''docker network create my-network'''
                sh '''docker-compose -f tests/frontend_tests/docker-compose.yml up -d'''
            }
        }
        stage('Deploying Services'){
            steps {
                sh '''docker-compose up -d --build'''
            }
        }
        stage('Testing'){
        parallel {
        stage('Backend Tests'){
                agent {
                        docker {
                            image 'qnib/pytest'
                            reuseNode true
                            args "--network my-network"
                            }
                       }
                steps {
                    sh '''pip install requests'''
                    sh '''pytest tests/backend_tests/user_app_tests/ --junit-xml=reports/tests.xml'''
                    }
                }
        stage('UI Tests'){
                agent {
                        docker {
                            image 'qnib/pytest'
                            reuseNode true
                            args "--network my-network"
                            }
                       }
                      steps{
                      sh '''pip install selenium'''
                      sh '''pytest tests/frontend_tests/ --junit-xml=reports/tests.xml'''
                    }
                }
            }
         }
      }
      post {
        always {
            junit 'reports/*.xml '
            sh '''docker-compose down'''
            sh '''docker-compose -f tests/frontend_tests/docker-compose.yml down'''
            sh '''docker network rm my-network'''
            sh '''docker system prune -af'''
            sh '''docker volume prune -f'''
        }
    }
}