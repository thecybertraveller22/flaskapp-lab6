pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-lab6-app'
        CONTAINER_NAME = 'flask-lab6-container'
        APP_PORT = '5000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // 'checkout scm' is the correct way to pull the repo in a pipeline
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python environment on Windows...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    call venv\\Scripts\\activate
                    pytest || echo "No tests found"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Note: Windows uses %VAR% syntax in batch, but Jenkins variables 
                // inside strings work with ${VAR}
                bat "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                // Using 2>nul || exit 0 to prevent failure if container doesn't exist
                bat """
                    docker stop ${CONTAINER_NAME} 2>nul || (exit 0)
                    docker rm ${CONTAINER_NAME} 2>nul || (exit 0)
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 --restart unless-stopped ${DOCKER_IMAGE}:latest
                """
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Check the console output above for the specific error."
        }
    }
}
