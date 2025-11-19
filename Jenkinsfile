pipeline {
    agent any
    
    tools {
        // CORRECTION: Replaced 'jenkinsScanner' with the correct tool alias 'sonar-scanner'.
        sonar-scanner 'SonarScanner' 
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/your-repository.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean install'
            }
        }

        stage('Static Code Analysis (SAST)') {
            steps {
                withSonarQubeEnv('SonarQube-Local') { 
                    bat 'sonar-scanner -Dsonar.projectKey=my_project -Dsonar.sources=./src'
                }
            }
        }

        stage('Dependency Check') {
            steps {
                // Note: Ensure the 'dependency-check' command is globally available on Windows PATH.
                bat 'dependency-check --project MyProject --scan ./ --format HTML --out dependency-check-report.html'
            }
        }
        
        // ... (Remaining stages) ...
    }
    
    // ... (Post stage) ...
}
