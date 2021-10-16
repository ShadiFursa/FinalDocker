pipeline {
	agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_shadi')
	}
        stages {
        	stage('Building our image') {
        		steps{
                		script {
                        		sh 'sudo docker build -t btcvalues .'
                		}
            		}
        	}	
        	stage('Login to Dockerhub') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}  
		stage('Push to Dockerhub') {
			steps {
				sh 'sudo docker tag btcvalues shadifursa/btcvalues'
				sh 'sudo docker push shadifursa/btcvalues'

			}
		}
    	}
}
