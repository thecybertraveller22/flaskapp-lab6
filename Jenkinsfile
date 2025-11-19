pipeline {
    agent any
    
    tools {
        // Load the SonarQube Scanner executable configured in Step 2
        // NOTE: Replace 'SonarScanner' if you used a different name.
        jenkinsScanner SonarScanner
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/your-repository.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Change to 'bat' for Windows Command Prompt compatibility
                bat 'mvn clean install'
            }
        }

        stage('Static Code Analysis (SAST)') {
            steps {
                // Recommended integration method: 'withSonarQubeEnv' automatically sets the URL and Token
                withSonarQubeEnv('SonarQube-Local') { // Use the name from Step 1
                    // The command is now simpler as Jenkins handles the Dsonar.host/login parameters
                    // Changed 'sh' to 'bat' for Windows compatibility
                    bat 'sonar-scanner -Dsonar.projectKey=my_project -Dsonar.sources=./src'
                }
            }
        }

        stage('Dependency Check') {
            steps {
                // WARNING: 'sh' commands may fail for these non-Java tools on Windows
                bat 'dependency-check --project MyProject --scan ./ --format HTML --out dependency-check-report.html'
            }
        }

        // ... (Remaining stages go here, using 'bat' for commands) ...
    }

    // ... (Post stage remains the same) ...
}
