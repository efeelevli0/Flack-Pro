[Setup]
AppName=Flack Pro
AppVersion=1.0
WizardStyle=modern
DefaultDirName={autopf}\Flack Pro
DefaultGroupName=Flack Pro
OutputBaseFilename=Flack_Pro_Setup
Compression=lzma
SolidCompression=yes
OutputDir=.\Setup_Ciktisi
SetupIconFile=flack_logo.ico

[Tasks]
Name: "desktopicon"; Description: "Masaüstü kısayolu oluştur"

[Files]
Source: "flack_pro.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "sesler\*"; DestDir: "{app}\sesler"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "flack_logo.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\Flack Pro"; Filename: "{app}\flack_pro.exe"; IconFilename: "{app}\flack_logo.ico"; Tasks: desktopicon
Name: "{group}\Flack Pro"; Filename: "{app}\flack_pro.exe"; IconFilename: "{app}\flack_logo.ico"

[Run]
Filename: "{app}\flack_pro.exe"; Description: "Flack Pro uygulamasını başlat"; Flags: nowait postinstall skipifsilent