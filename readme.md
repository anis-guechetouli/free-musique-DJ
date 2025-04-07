# 🎵 YouTube Audio Downloader

Une application de bureau simple et rapide développée en **Python**, permettant de rechercher des vidéos YouTube et de télécharger directement l’audio au format **MP3**.

## ✨ Fonctionnalités

- 🔍 Rechercher des vidéos sur YouTube via l'API officielle
- 🎧 Télécharger uniquement l’audio au format MP3
- 📁 Choisir le dossier de destination pour enregistrer les fichiers
- 🖥️ Interface graphique conviviale avec Tkinter

## 🛠️ Technologies utilisées

- Python 3
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg
- Tkinter
- API YouTube Data v3

## 📦 Installation

### Prérequis

- Python 3.8+
- FFmpeg installé et accessible dans le `PATH`
- Une clé API YouTube (à obtenir via [Google Cloud Console](https://console.cloud.google.com/))

### Étapes

1. Clone le dépôt :

```bash
git clone https://github.com/ton-utilisateur/youtube-audio-downloader.git
cd youtube-audio-downloader
```

2. Installe les dépendances :

```bash
pip install -r requirements.txt
```
3. Remplace la clé API dans le fichier main.py par la tienne :

````bash
api_key = 'VOTRE_CLE_API_ICI'
````
4. Lance l'application :

```bash
python main.py
