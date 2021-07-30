pipeline {
    agent any
    stages {
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
              sh '''docker rm -f $(docker ps -a -q)'''
              sh '''docker system prune -af'''
              sh '''docker volume prune -f'''
        }
    }
  }