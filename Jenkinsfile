node {
    stage('checkout'){
        checkout scm
    }
    stage('build'){
        sh '''docker-compose up -d --build '''
    }
    stage('teardown'){
        sh '''docker-compose down '''
}
}
//