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
                // This fix ensures exit code 5 (no tests found) doesn't stop the build
                bat '''
                    call venv\\Scripts\\activate
                    pytest || (if %errorlevel%==5 (exit 0) else (exit %errorlevel%))
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                bat """
                    docker stop ${CONTAINER_NAME} 2>nul || (exit 0)
                    docker rm ${CONTAINER_NAME} 2>nul || (exit 0)
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 --restart unless-stopped ${DOCKER_IMAGE}:latest
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completed! App available at http://localhost:5000"
        }
        failure {
            echo "Pipeline failed. Check the console output above for the specific error."
        }
    }
}
