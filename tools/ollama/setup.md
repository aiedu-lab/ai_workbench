# Tool Guide: Local AI Setup (Ollama)

AI models are heavy. Before we download a "brain," we need to ensure our computer has the space and memory to hold it. Follow the instructions below for your specific Operating System.

---

## 🍎 macOS Setup (Apple Silicon & Intel)

### 1. Capacity Audit
Macs handle memory very efficiently. If you have an Apple Silicon chip (M1, M2, M3), your CPU and GPU share the same memory (Unified Memory), making it incredible for AI.
1. Click the **Apple Logo** in the top left corner.
2. Click **About This Mac**.
3. Look at the **Memory** value.

**Mac Model Selection Guide:**
* **8 GB Memory:** Run the lightweight model: `ollama pull gemma:2b`
* **16 GB Memory or higher:** Run the heavyweight model: `ollama pull llama3:8b`

### 2. Installation
1. Go to [Ollama.com/download](https://ollama.com/download/mac).
2. Download the Mac version.
3. Unzip the file and drag **Ollama.app** into your Applications folder.
4. Open the app. You will see a small llama icon appear in your top menu bar.
5. Open your **Terminal** app and run your chosen pull command (e.g., `ollama pull llama3:8b`).

---

## 🪟 Windows Setup

### 1. Capacity Audit
Windows handles System RAM and Graphics Card Memory (VRAM) separately. We have a script to check your exact capacity.
1. Open **Windows PowerShell**.
2. Copy and paste this script, then press Enter:

    ```powershell
    Write-Host "--- AI Local System Audit ---" -ForegroundColor Cyan
    $ram = Get-CimInstance Win32_ComputerSystem | Select-Object @{Name="TotalRAM_GB";Expression={[math]::Round($_.TotalPhysicalMemory/1GB, 1)}}
    Write-Host "System RAM: $($ram.TotalRAM_GB) GB"
    
    $disk = Get-Volume -DriveLetter C
    Write-Host "Free Disk Space: $([math]::Round($disk.SizeRemaining/1GB, 1)) GB"
    
    Write-Host "Graphics Cards:"
    Get-CimInstance Win32_VideoController | ForEach-Object {
        $vram = [math]::Round($_.AdapterRAM/1GB, 1)
        if ($vram -gt 0 -and $vram -lt 100) { Write-Host " - $($_.Name) (VRAM: ~$vram GB)" }
        else { Write-Host " - $($_.Name) (Shared Memory)" }
    }
    Write-Host "-----------------------------" -ForegroundColor Cyan
    ```

**Windows Model Selection Guide:**
* **8 GB System RAM** OR **Less than 4GB VRAM:** Run the lightweight model: `ollama pull gemma:2b`
* **16 GB+ System RAM** OR **6 GB+ VRAM:** Run the heavyweight model: `ollama pull llama3:8b`

### 2. Installation
1. Go to [Ollama.com/download](https://ollama.com/download/windows).
2. Download the Windows installer (`.exe`) and run it.
3. Ensure the Ollama icon is running in your system tray (bottom right).
4. Open **PowerShell** (or your WSL terminal) and run your chosen pull command (e.g., `ollama pull llama3:8b`).
