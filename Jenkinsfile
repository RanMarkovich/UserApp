pipeline {
    agent any
    stages {
        stage('prepare environment'){
         agent {
                docker { image 'python:3.9' }
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
         agent {
                docker { image 'python:3.9' }
            }
            steps {  withEnv(["HOME=${env.WORKSPACE}"]) {sh '''pytest tests/user_app_tests/''' }}
        }
    }
  }