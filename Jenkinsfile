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
                sh 'python -m venv venv'
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
                sh 'venv/Scripts/activate'
                sh 'pip install -r ./MuonTraSach/requirements.txt'
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
                sh 'venv/Scripts/activate'
                sh 'cd MuonTraSach'
                sh 'python -m MuonTraSach.test.test_login'
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
                sh 'venv/Scripts/activate'
                sh 'cd MuonTraSach'
                sh 'python -m MuonTraSach.index'
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
