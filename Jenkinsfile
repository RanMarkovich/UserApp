node {
    stage('checkout'){
    git 'https://github.com/RanMarkovich/UserApp.git'
    }
    stage('build'){
        sh '''docker-compose up -d --build '''
    }
    stage('teardown'){
        sh '''docker-compose down '''
}
}
////// /