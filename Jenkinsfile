pipeline {
    agent { label 'jenkins_slave_1'}
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
                            image 'ranmarkovich/python_pytest_selenium'
                            reuseNode true
                            args "--network my-network"
                            }
                       }
                steps {
                    sh '''pytest --alluredir="tests/reports/allure_results" -vvv --env=remote tests/backend_tests/user_service/ --junit-xml=reports/be_tests.xml'''
                    }
                }
        stage('UI Tests'){
                agent {
                        docker {
                            image 'ranmarkovich/python_pytest_selenium'
                            reuseNode true
                            args "--network my-network"
                            }
                       }
                      steps{
                      sh '''pytest --alluredir="tests/reports/allure_results" -vvv --env=remote tests/frontend_tests/ --junit-xml=reports/fe_tests.xml'''
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
