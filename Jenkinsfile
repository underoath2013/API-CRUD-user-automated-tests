pipeline {
    agent any

    environment {
        ALLURE_PATH = '/home/linuxbrew/.linuxbrew/bin/allure'
        POSTGRES_HOST: 'fast-api-user-example-postgresql-1'
        HOST: 'http://fast-api-user-example-api-1:8000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: '*/main']],
                extensions: [],
                submoduleCfg: [],
                userRemoteConfigs: [[url: 'https://github.com/underoath2013/API-CRUD-user-automated-tests.git']]])
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                    """
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${ALLURE_RESULTS}"]]
                ])
            }
        }
    }
}
