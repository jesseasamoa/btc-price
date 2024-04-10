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
                pip install pandas sqlalchemy python-binance
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                source venv/bin/activate
                python3 add.py
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
