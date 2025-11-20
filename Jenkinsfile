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
        // REMOVED: Redundant 'Checkout' stage. Jenkins checks out the SCM automatically.
        
        stage('Build') {
            steps {
                echo "Build step..."
            }
        }
        
        stage('SonarCloud Analysis') {
            steps {
                // IMPORTANT: The 'sonarcloud-token' credential ID MUST exist in Jenkins (Type: Secret Text)
                withCredentials([string(credentialsId: 'sonarcloud-token', variable: 'TOKEN')]) {
                    
                    // You must manually specify all parameters for SonarCloud
                    bat """
                        // Path to scanner executable is correctly retrieved using the 'tool' function
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
