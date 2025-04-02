pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                script {
                    // Activate the virtual environment and run pytest
                    bat '''@echo off
                    REM Activate the virtual environment
                    call E:\\UIC\\RAE\\Labs\\Lab 6\\mliplab6\\mlip\\myenv\\Scripts\\activate.bat

                    REM Run pytest for testing
                    pytest

                    REM Deactivate the virtual environment after running tests
                    deactivate
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our project'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
