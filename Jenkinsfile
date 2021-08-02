pipeline {
    agent { label 'master' }
    stages{
        stage('build'){
        agent { label 'agent1' }
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
            agent { label 'agent1' }
           steps { sh '''docker-compose down '''}
      }
   }
}//