pipeline {
    agent any
    stages {
        stage('Docker Build') {
            steps {
               sh 'docker build -f Dockerfile -t rondocker8511/rondockerrep:testjenkinsdocker .'
            }
        }
        stage('Docker Push') {
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
        stage('Kubectl Deployment') {
            steps {
               sh 'kubectl create deployment rondep --port 5000 -r 2 -n ronns --image rondocker8511/rondockerrep:testjenkinsdocker'
            }
        }
        stage('Kubectl Expose') {
            steps {
               sh 'kubectl expose deployment rondep -n ronns --type=ClusterIP --port=5000'
            }
        }
    }
}