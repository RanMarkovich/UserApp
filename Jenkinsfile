pipeline {
    agent { label 'master' }
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
       post {
        always {
            sh '''docker-compose down'''
        }
      }
   }
}
