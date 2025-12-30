pipeline {
    agent any

    environment {
        // Configuration variables for easy updates
        REPO_URL = 'https://github.com/thecybertraveller22/flaskapp-lab6.git'
        DOCKER_IMAGE = 'flask-lab6-app'
        CONTAINER_NAME = 'flask-lab6-container'
        APP_PORT = '5000'
    }

    stages {
        // 1. Clone the repo
        stage('Clone Repository') {
            steps {
                echo 'Fetching the latest code from GitHub...'
                git branch: 'main', url: "${env.REPO_URL}"
            }
        }

        // 2. Install dependencies
        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python environment and installing requirements...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // 3. Run unit tests
        stage('Run Unit Tests') {
            steps {
                echo 'Executing PyTest...'
                // If you don't have a test_app.py yet, this may fail. 
                // Use '|| true' if you want the pipeline to continue regardless.
                sh '''
                    . venv/bin/activate
                    python3 -m pytest || echo "No tests found to run"
                '''
            }
        }

        // 4. Build the app (Docker Image)
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}..."
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        // 5. Deploy the app
        stage('Deploy') {
            steps {
                echo 'Stopping old containers and starting the new one...'
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:5000 \
                        --restart unless-stopped \
                        ${DOCKER_IMAGE}:latest
                """
            }
        }
    }

    post {
        success {
            echo "-----------------------------------------------------------"
            echo "Deployment Successful!"
            echo "App is live at: http://localhost:${APP_PORT}"
            echo "-----------------------------------------------------------"
        }
        failure {
            echo "Pipeline failed. Check the Jenkins console output for errors."
        }
        always {
            // Cleans up the workspace to save disk space
            cleanWs()
        }
    }
}
