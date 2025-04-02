pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''echo "In C or Java, we can compile our program in this step"
                      echo "In Python, we can build our package here or skip this step"
                   '''
            }
        }
        stage('Test') {
            steps {
                bat '''echo "Test Step: We run testing tool like pytest here"

                      REM Activate the venv environment (replace with your path)
                      call "E:\\UIC\\RAE\\Labs\\Lab 6\\mliplab6\\mlip\\Scripts\\activate.bat"

                      REM Run pytest command within the activated environment
                      pytest

                      echo "pytest ran successfully"
                   '''
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
