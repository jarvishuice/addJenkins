pipeline {
    agent any

    stages {
        stage('Preparar Entorno') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Ejecutar Pruebas') {
            steps {
                sh 'python -m pytest tests/'
            }
        }
        
        stage('Construir') {
            steps {
                sh 'echo "Construcción completada"'
            }
        }
        
        stage('Desplegar') {
            steps {
                sh '''
                    echo "Iniciando despliegue..."
                    # Aquí puedes agregar comandos para desplegar tu aplicación
                    # Por ejemplo: reiniciar el servicio uvicorn
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado exitosamente!'
        }
        failure {
            echo 'El pipeline ha fallado'
        }
    }
}