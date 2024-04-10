pipeline {
    agent { 
        node {
            label 'python-cloud'
        }
    }
    triggers {
        pollSCM('*/4 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install pandas
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                source venv/bin/activate
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
