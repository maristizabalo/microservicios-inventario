import os
import subprocess
from pathlib import Path

services = {
    "auth": 8001,
    "inventory": 8002,
    "movement": 8003,
    "api_gateway": 8004,
}

base_dir = Path(__file__).parent.resolve()

def run_powershell(cmd, cwd):
    full_cmd = ["powershell", "-Command", cmd]
    subprocess.run(full_cmd, cwd=cwd)

for service, port in services.items():
    service_path = base_dir / service
    venv_path = service_path / 'venv'

    print(f"\n=== Configurando {service} ===")

    # Crear entorno virtual si no existe
    if not venv_path.exists():
        print(f"Creando entorno virtual para {service}...")
        run_powershell(f"python -m venv venv", service_path)

    # Instalar requirements
    pip_path = venv_path / 'Scripts' / 'pip'
    run_powershell(f"{pip_path} install -r requirements.txt", service_path)

    # Django: makemigrations y migrate
    python_path = venv_path / 'Scripts' / 'python'
    run_powershell(f"{python_path} manage.py makemigrations", service_path)
    run_powershell(f"{python_path} manage.py migrate", service_path)

    # Levantar runserver en otro powershell separado
    print(f"Levantando {service} en el puerto {port}...")
    run_powershell(f"Start-Process powershell -ArgumentList 'cd {service_path}; .\\venv\\Scripts\\activate; {python_path} manage.py runserver 0.0.0.0:{port}'", service_path)

print("\n🚀 Todos los microservicios se están levantando en sus respectivos puertos.")
