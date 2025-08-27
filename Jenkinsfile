pipeline {
    agent any
        options {
        skipDefaultCheckout(false)
    }

    stages {
        stage('Debug Info') {
            steps {
                echo "Branch: ${env.BRANCH_NAME}"
                echo "Is PR: ${env.CHANGE_ID != null}"
                echo "Target branch: ${env.CHANGE_TARGET}"
            }
        }
        stage('Prepare Environment') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                }
            }
            steps {
                bat 'rm -rf venv'
                bat 'py -3.12 -m venv venv'
                bat '.\\venv\\Scripts\\pip install --upgrade pip'
            }
        }

        stage('Install ') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                }
            }
            steps {
                bat '.\\venv\\Scripts\\pip install -r ./MuonTraSach/requirements.txt'
            }
        }

        stage('Test') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                }
            }
            steps {
                bat '.\\venv\\Scripts\\activate'
                bat 'cd MuonTraSach'
                bat 'python -m MuonTraSach.test.test_login'
            }
        }

        stage('Build') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                }
            }
            steps {
                echo "Building project on main..."
            }
        }

        stage('Deploy') {
            when {
                anyOf {
                    changeRequest()
                    branch 'main'
                }
            }
            steps {
                bat '.\\venv\\Scripts\\activate'
                bat 'cd MuonTraSach'
                bat 'python -m MuonTraSach.index'
            }
        }
    }
    post {
        failure {
            echo " Pipeline failed. Please check the logs."
        }
        success {
            echo " Pipeline succeeded!"
        }
        aborted {
            echo " Pipeline was aborted."
        }
    }
}
