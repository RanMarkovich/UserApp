pipeline {
    agent any
    stages {
        stage('prepare environment'){
         agent {
                docker { image 'python:3.9-alpine' }
            }
            steps {  withEnv(["HOME=${env.WORKSPACE}"]) {sh '''pip install -r tests/requirements.txt''' }}
        }
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
            steps { sh '''pytest tests/user_app_tests/''' }
        }
    }
    post {
        always {
              sh '''docker-compose down'''
              sh '''docker rm -f $(docker ps -a -q)'''
              sh '''docker system prune -af'''
              sh '''docker volume prune -f'''
        }
    }
  }