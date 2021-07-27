pipeline {
    agent { label 'master' }
    stages{
        stage('checkout'){
            steps { checkout scm }
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
        stage('teardown'){
           steps { sh '''docker-compose down '''}
      }
   }
}
