pipeline {
    agent any
    enviroment{
	DOCKERHUB_CREDENTIALS=credentials('dockerhub_shadi')
    }
    stages {
	stage('Building our image') {
            steps{
                script {
                	sh 'sudo -s docker build -t btcvalues .'
         	}
	    }
        }
	stage('login to dockerhub'){
	    steps{
	    	sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'	
	    }
	}
	stage('push to dockerhub'){
	    steps{
		sh 'sudo docker tag btcvalues shadifursa/btcvalues'
		sh 'sudo docker push shadifursa/btcvalues'
	    }
	}
	
    }
}

