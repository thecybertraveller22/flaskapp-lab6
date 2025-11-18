pipeline {
    agent any
    
    // 1. Tools Section (From Image 3)
    tools {
        // Make sure you named your Maven tool 'Maven' in Jenkins settings!
        maven 'Maven'
    }

    // 2. Parameters Section (From Image 1)
    parameters {
        // I selected 'choice' instead of 'string' so you get a dropdown menu
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Version to deploy')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run tests?')
    }

    // 3. Environment Variables (From Image 1)
    environment {
        NEW_VERSION = '1.3.0'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Project'
                
                // Using the environment variable (From Image 3)
                echo "Building version ${NEW_VERSION}"
                
                // Installing NVM (Changed 'sh' to 'bat' for Windows)
                bat "nvm install"
            }
        }
        
        stage('Test') {
            // 4. Conditional Execution (From Image 2)
            // This stage ONLY runs if the checkbox 'executeTests' is checked
            when {
                expression { params.executeTests }
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
