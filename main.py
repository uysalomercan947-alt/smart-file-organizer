import os
import shutil
from datetime import datetime

def organize_my_folder():
    # Mevcut klasördeki dosyaları tara
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
    
    # Git veya Python dosyalarını yanlışlıkla taşımamak için filtrele
    ignore_files = ["main.py", ".gitignore"]
    
    # Dosya türü eşleştirmeleri
    file_types = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Audio_Video": [".mp3", ".mp4", ".wav", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"]
    }
    
    moved_count = 0
    report_lines = []

    for file in files:
        if file in ignore_files:
            continue
            
        file_ext = os.path.splitext(file)[1].lower()
        target_folder = "Others" # Bilinmeyen uzantılar için varsayılan klasör
        
        # Uzantıya göre doğru klasörü bul
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = folder
                break
                
        # Hedef klasör yoksa oluştur
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
        # Dosyayı taşı
        try:
            shutil.move(file, os.path.join(target_folder, file))
            report_lines.append(f"SUCCESS: Moved '{file}' to '{target_folder}/'")
            moved_count += 1
        except Exception as e:
            report_lines.append(f"ERROR: Could not move '{file}'. Reason: {str(e)}")

    # İngilizce Rapor (Log) Dosyası Oluşturma - Global kullanıcılar için
    if moved_count > 0:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_filename = "folder_organizer_report.txt"
        
        with open(report_filename, "a", encoding="utf-8") as f:
            f.write(f"\n=== Run Session: {timestamp} ===\n")
            f.write(f"Total files organized: {moved_count}\n")
            f.write("\n".join(report_lines))
            f.write("\n===================================\n")
            
        print(f"🎉 Success! Organized {moved_count} files. Check 'folder_organizer_report.txt' for details.")
    else:
        print("🔍 No clutter found! The folder is already clean.")

if __name__ == "__main__":
    organize_my_folder()
