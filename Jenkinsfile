def flag = true  // 1. Variable defined here

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Project'
            }
        }
        
        stage('Test') {
            // 2. This stage runs ONLY if the condition matches
            when {
                expression { flag == false } 
            }
            steps {
                echo 'Testing Project'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    post {
        always {
            echo 'Post build condition running'
        }
        failure {
            echo 'Post action if build failed'
        }
    }
}
