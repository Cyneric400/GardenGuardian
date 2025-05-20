Set-Location C:\Users\write\source\GardenGuardian\Scripts
.\activate.ps1
Set-Location C:\Users\write\PycharmProjects\GardenGuardian
streamlit run main.py

Write-Host "Exiting streamlit server and virtual environment..."
.\deactivate.bat