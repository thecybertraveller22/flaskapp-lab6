pipeline {
    agent any

    // --- GLOBAL TOOLS ---
    tools {
        // MANDATORY FIX: Using the full, definitive syntax for the SonarQube Scanner tool.
        tool name: 'SonarScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // IMPORTANT: Replace 'https://github.com/your-repository.git' with your actual repo URL
                git url: 'https://github.com/your-repository.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Use 'bat' for Windows command compatibility
                bat 'mvn clean install' 
            }
        }

        stage('Static Code Analysis (SAST)') {
            steps {
                // RECOMMENDED: This step automatically injects sonar.host.url and sonar.login (API Token)
                withSonarQubeEnv('SonarQube-Local') { 
                    // The command is simpler now; Jenkins handles URL/Token injection.
                    bat 'sonar-scanner -Dsonar.projectKey=my_project -Dsonar.sources=./src'
                }
            }
        }

        stage('Dependency Check') {
            steps {
                // Uses 'bat' for Windows compatibility
                bat 'dependency-check --project MyProject --scan ./ --format HTML --out dependency-check-report.html'
            }
        }

        stage('Container Security Scan') {
            steps {
                // WARNING: Trivy (and Docker) must be installed and accessible on your Windows PATH
                bat 'trivy image myapp:latest' 
            }
        }

        stage('Unit Tests') {
            steps {
                bat 'mvn test'
            }
        }

        stage('Deploy to Staging') {
            steps {
                // WARNING: kubectl must be installed and configured on your Windows PATH
                bat 'kubectl apply -f k8s-deployment.yaml'
            }
        }

        stage('Security Gate') {
            steps {
                // Reads the dependency check report and aborts the pipeline if high risk is found
                script {
                    def hasVulnerabilities = readFile('dependency-check-report.html').contains('High')
                    if (hasVulnerabilities) {
                        error "Security vulnerabilities found. Aborting the pipeline!"
                    }
                }
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                // Only runs if security checks passed and branch is 'main'
                bat 'kubectl apply -f k8s-prod-deployment.yaml'
            }
        }
    }

    post {
        always {
            // Archives reports regardless of success/failure
            archiveArtifacts artifacts: 'dependency-check-report.html, sonar-report.html', allowEmptyArchive: true
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
