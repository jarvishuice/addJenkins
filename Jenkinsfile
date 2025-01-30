pipeline {
    agent any

    stages {
        stage('Preparar Entorno') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Ejecutar Pruebas') {
            steps {
                bat 'python -m pytest tests/'
            }
        }
        
        stage('Construir') {
            steps {
                bat 'echo "Construcción completada"'
            }
        }
        
        stage('Desplegar') {
            steps {
                bat '''
                    echo "Iniciando despliegue..."
                    rem Aquí tus comandos de despliegue para Windows
                '''
            }
        }
    }

    post {
        success {
            bat 'echo "Pipeline ejecutado exitosamente!"'
        }
        failure {
            bat 'echo "El pipeline ha fallado"'
        }
    }
}