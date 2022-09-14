pipeline {
  agent any
  environment {
    ARTIFACTORY_CREDS = credentials('GITHUB_ARTIFACTORY_TOKEN')
  }
  parameters {
        string(
            name: 'API_URL',
            defaultValue: 'https://reqres.in/api/users',
            description: '''<h3>API URL</h3>'''
        )
  }
  stages {
    stage('Generate User Data') {
      steps {
        sh "python3 generateDevOpsUserData.py --url ${params.API_URL}"
      }
    }
    stage('Test'){
      steps {
        sh "coverage run -m pytest"
        sh "coverage report -m"
        sh "coverage html"
      }
    }
    stage('Deploy') {
      steps {
        sh """
          zip devops-user-data-docs.zip -r devops-user-data*
          curl -u ${env.ARTIFACTORY_CREDS} -XPUT "https://codingchallenge.jfrog.io/artifactory/coding-challenge/${currentBuild.number}/" -T devops-user-data-docs.zip
        """
      }
    }
  }
}
