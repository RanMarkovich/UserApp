pipeline {
    agent {label 'master'}
    stages {
        stage('prepare environment'){
         agent {
                docker { image 'python:3.9' }
            }
            steps {  withEnv(["HOME=${env.WORKSPACE}"]) {sh '''pip install -r tests/requirements.txt''' }}
        }
        stage('build'){
                agent {
                docker { image 'jenkins/ssh-agent' args '-it --entrypoint=/bin/bash'}
            }
            steps {
                    sh '''docker-compose up -d --build '''
           }
        }
        stage('test'){
        agent {
                docker { image 'python:3.9' }
            }
            steps { sh '''pytest tests/user_app_tests/''' }
        }
        stage('teardown'){
        agent {
                docker { image 'jenkins/ssh-agent' }
            }
           steps { sh '''docker-compose down '''}
      }
    }
  }