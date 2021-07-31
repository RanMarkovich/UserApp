pipeline {
    agent { docker { image 'jenkins/ssh-agent' } }
    stages {
        stage('requirements') {
          steps {
            sh 'pip install -r tests/requirements.txt'
          }
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
              sh '''docker rm -f $(docker ps -a -q)'''
              sh '''docker system prune -af'''
              sh '''docker volume prune -f'''
        }
    }
  }