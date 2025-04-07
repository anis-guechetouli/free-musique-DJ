import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import requests

# Variable globale pour stocker les vidéos trouvées
videos = []

# Fonction pour rechercher les vidéos sur YouTube via l'API YouTube Data
def search_youtube(query):
    api_key = 'ici la cle api youtube'  # Remplacez par votre clé API YouTube
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&maxResults=10&key={api_key}"
    response = requests.get(url)
    results = response.json()
    
    vids = []
    for item in results['items']:
        # Vérification pour s'assurer qu'il s'agit bien d'une vidéo
        if 'videoId' in item['id']:
            title = item['snippet']['title']
            description = item['snippet']['description']
            video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            vids.append((title, description, video_url))
    return vids

# Fonction pour télécharger uniquement l'audio de la vidéo sélectionnée dans un dossier choisi
def download_audio(video_url, download_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        # Le fichier sera enregistré dans le dossier choisi
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Chemin vers ffmpeg
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            messagebox.showinfo("Succès", "Téléchargement terminé avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")

# Fonction pour gérer le clic sur le bouton de recherche
def search_videos():
    global videos  # Pour rendre la variable accessible globalement
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Avertissement", "Veuillez entrer un terme de recherche.")
        return
    
    videos = search_youtube(query)
    video_listbox.delete(0, tk.END)  # Effacer la liste précédente
    if videos:
        for idx, (title, description, url) in enumerate(videos, 1):
            video_listbox.insert(tk.END, f"{idx}. {title}")
    else:
        messagebox.showwarning("Avertissement", "Aucune vidéo trouvée.")

# Fonction pour gérer le clic sur le bouton de téléchargement
def on_download_button_click():
    try:
        selected_index = video_listbox.curselection()[0]  # Récupérer l'index de la vidéo sélectionnée
        video_url = videos[selected_index][2]  # Obtenir l'URL de la vidéo sélectionnée
        # Demander à l'utilisateur de choisir le dossier de destination
        download_folder = filedialog.askdirectory(title="Choisissez le dossier de destination")
        if not download_folder:
            messagebox.showwarning("Avertissement", "Aucun dossier sélectionné.")
            return
        download_audio(video_url, download_folder)
    except IndexError:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une vidéo à télécharger.")

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Téléchargeur Audio YouTube")

# Champ de recherche
search_label = tk.Label(root, text="Entrez le terme de recherche :")
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Rechercher", command=search_videos)
search_button.pack(pady=5)

# Liste des vidéos trouvées
video_listbox = tk.Listbox(root, width=50, height=10)
video_listbox.pack(pady=5)

# Bouton pour télécharger l'audio de la vidéo sélectionnée
download_button = tk.Button(root, text="Télécharger l'audio", command=on_download_button_click)
download_button.pack(pady=5)

# Lancer l'application
root.mainloop()
