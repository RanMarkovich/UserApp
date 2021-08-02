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
        stage('teardown'){
           steps { sh '''docker-compose down '''}
      }
   }
}//