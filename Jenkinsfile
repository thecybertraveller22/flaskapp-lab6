pipeline {
    agent any

    // Ensure SonarScanner is installed and named 'SonarScanner' in Manage Jenkins > Tools
    tools {
        hudson.plugins.sonar.SonarRunnerInstallation('SonarScanner') 
    }

    environment {
        PROJECT = "thecybertraveller22_flaskapp-lab6"
        ORG = "thecybertraveller22"
    }

    stages {
        
        // **REMOVED THE REDUNDANT 'Checkout' STAGE HERE**
        // Jenkins handles the checkout automatically (Declarative: Checkout SCM)

        stage('Build') {
            steps {
                echo "Build step..."
                // Add your actual build command here, e.g., bat 'mvn clean install'
            }
        }
        
        stage('SonarCloud Analysis') {
            steps {
                // IMPORTANT: The 'sonarcloud-token' credential ID MUST exist in Jenkins (Type: Secret Text)
                withCredentials([string(credentialsId: 'sonarcloud-token', variable: 'TOKEN')]) {
                    
                    // NOTE: Since you are using SonarCloud, the 'withSonarQubeEnv' wrapper is NOT needed,
                    // as you are manually specifying all parameters (URL, login, etc.) below.
                    
                    bat """
                        // Full path to scanner executable is correctly retrieved using the 'tool' function
                        ${tool 'SonarScanner'}\\bin\\sonar-scanner.bat ^
                          -Dsonar.projectKey=${PROJECT} ^
                          -Dsonar.organization=${ORG} ^
                          -Dsonar.sources=. ^
                          -Dsonar.host.url=https://sonarcloud.io ^
                          -Dsonar.login=%TOKEN% ^
                          -Dsonar.c.file.suffixes=- ^
                          -Dsonar.cpp.file.suffixes=- ^
                          -Dsonar.objc.file.suffixes=-
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // This step is critical for continuous integration: it fails the build if the code fails the quality check.
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status == 'NONE') {
                            echo "Warning: No quality gate configured. Proceeding with build."
                        } else if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deployment step..."
            }
        }
    }
}
