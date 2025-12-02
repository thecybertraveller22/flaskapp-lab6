pipeline {
    agent any

    // Lab 13 Contribution: Added Quality Gate stage - Syed Arham Ahmed (22i-1552) developer2
    

    environment {
        PROJECT = "thecybertraveller22_flaskapp-lab6"
        ORG = "thecybertraveller22"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/thecybertraveller22/flaskapp-lab6.git'
            }
        }

        stage('Build') {
            steps {
                echo "Build step..."
            }
        }
        stage('SonarCloud Analysis') {
            steps {
                withCredentials([string(credentialsId: 'Ronaldo', variable: 'TOKEN')]) {
                    withSonarQubeEnv('SonarCloud') {
                        bat """
                            ${tool 'SonarScanner'}\\bin\\sonar-scanner.bat ^
                              -Dsonar.projectKey=thecybertraveller22_flaskapp-lab6 ^
                              -Dsonar.organization=thecybertraveller22 ^
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