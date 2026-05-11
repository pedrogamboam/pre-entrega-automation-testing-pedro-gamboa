# Pre-entrega Automation Testing - Pedro Gamboa

## Propósito
Este proyecto automatiza el flujo de login, navegación y carrito de compras en [SauceDemo](https://www.saucedemo.com) utilizando Selenium WebDriver y Pytest.

## Tecnologías utilizadas
- Python 3.13
- Selenium
- Pytest
- Pytest-HTML
- Git y GitHub

## Instalación
Clonar el repositorio y ejecutar:
```bash
pip install -r requirements.txt

## Script de ejecución recomendado

Para correr los tests con el `PYTHONPATH` configurado y generar el reporte HTML automáticamente, usar el siguiente comando en PowerShell desde la carpeta raíz del proyecto:

```powershell
$env:PYTHONPATH="." ; pytest -v --html=reports/reporte.html --self-contained-html
