pipeline {
    agent { 
        node {
            label 'python-cloud'
        }
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install pandas
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 get-btc-price.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
