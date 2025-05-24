pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', credentialsId: '6dfa8ed5-4328-4c3a-9b56-ba73d9ee9ea5', url: 'https://github.com/ronslim/dockkubflaskjenkins'
                echo "Git Checkout Completed"
            }
        }
        stage('DockerBuild') {
            steps {
               sh 'docker build -f Dockerfile -t rondocker8511/rondockerrep:testjenkinsdocker .'
            }
        }
        stage('DockerPush') {
            steps {
               script {
               // This step should not normally be used in your script. Consult the inline help for details.
               withDockerRegistry(credentialsId: '9f16c357-a12b-4245-9f1f-b37e817e74fb') {
                   // some block
                  sh 'docker push rondocker8511/rondockerrep:testjenkinsdocker'
                  }
               }
            }
        }
        stage('KubernetesDeployment') {
            steps {
               sh 'kubectl create deployment rondep --port 5000 -r 2 -n ronns --image rondocker8511/rondockerrep:testjenkinsdocker'
            }
        }
        stage('KubernetesExpose') {
            steps {
               sh 'kubectl expose deployment rondep -n ronns --type=ClusterIP --port=5000'
            }
        }
    }
}