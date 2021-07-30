pipeline {
            agent {
                docker { image 'python:3.9' }
            }
    stages {
        stage('prepare environment'){

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
        stage('teardown'){
           steps { sh '''docker-compose down '''}
      }
    }
  }