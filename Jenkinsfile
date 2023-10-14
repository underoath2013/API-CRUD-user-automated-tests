pipeline {
    agent any

    environment {
        ALLURE_PATH = '/home/linuxbrew/.linuxbrew/bin/allure'
        POSTGRES_HOST = 'fast-api-user-example-postgresql-1'
        HOST = 'http://fast-api-user-example-api-1:8000'
    }

    parameters {
        string(name: 'ALLURE_RESULTS', defaultValue: 'allure-results', description: 'Path to Allure results directory')

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
                    rm -rf allure-report
                    rm -rf allure-results
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                    \${ALLURE_PATH} generate \${ALLURE_RESULTS} -c
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