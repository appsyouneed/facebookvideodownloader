# FB Video Downloader

An Android app that downloads Facebook videos and Reels to `DCIM/Facebook Downloads`.  
Works via manual URL paste **and** via the system **Share → Share to** flow from the Facebook app.

---

## Features

- 📲 **Share from Facebook app** — tap Share → FB Video Downloader, download starts automatically
- 🔗 **Paste URL manually** — paste any Facebook video/reel link and tap Download
- 📂 **Saves to `DCIM/Facebook Downloads`** — appears in your Gallery
- ⬇️ **Highest available quality** — tries HD first, falls back to SD
- 📊 **Progress tracking** — real-time MB downloaded / total
- 🔔 **Notification** — shows progress in notification drawer (foreground service)
- ✅ **Android 7–14+ support** — uses MediaStore on Android 10+, legacy path on Android 9 and below

---

## Supported URL formats

| Format | Example |
|--------|---------|
| Standard video | `https://www.facebook.com/username/videos/123456789` |
| Watch URL | `https://www.facebook.com/watch/?v=123456789` |
| Reel | `https://www.facebook.com/reel/123456789` |
| Short link | `https://fb.watch/aBcDeF` |
| Mobile URL | `https://m.facebook.com/reel/123456789` |
| video.php | `https://www.facebook.com/video.php?v=123456789` |

---

## Build Instructions

### Prerequisites
- Android Studio Hedgehog (2023.1.1) or newer
- JDK 11+
- Android SDK 34

### Steps

```bash
git clone <repo-url>
cd FacebookVideoDownloader

# Optional: generate launcher icon PNGs
pip install Pillow
python generate_icons.py

# Open in Android Studio, or build from command line:
./gradlew assembleDebug
```

The APK will be at:  
`app/build/outputs/apk/debug/app-debug.apk`

---

## How to use

### Method 1 — Share from Facebook
1. Open any Facebook video or Reel
2. Tap **Share** (bottom of post)
3. Tap **Share to** (or the external share icon)
4. Select **FB Video Downloader**
5. Download starts automatically

### Method 2 — Manual paste
1. Copy the video URL from Facebook
2. Open FB Video Downloader
3. Tap **Paste** or paste manually
4. Tap **Download Video**

---

## Project structure

```
app/src/main/
├── java/com/fbdownloader/
│   ├── MainActivity.kt           # UI + share intent handling
│   ├── MainViewModel.kt          # State management
│   ├── MainViewModelFactory.kt   # ViewModel factory
│   ├── UiState.kt                # Sealed UI states
│   ├── UrlExtractor.kt           # URL detection & validation
│   ├── FacebookVideoDownloader.kt # Core download + parsing logic
│   └── DownloadService.kt        # Foreground service + notifications
├── res/
│   ├── layout/activity_main.xml  # Main screen layout
│   ├── values/                   # Strings, colors, themes
│   ├── xml/network_security_config.xml
│   └── drawable/                 # Vector icons
└── AndroidManifest.xml           # Permissions + intent filters
```

---

## Permissions

| Permission | Why |
|-----------|-----|
| `INTERNET` | Fetch Facebook pages and download video files |
| `WRITE_EXTERNAL_STORAGE` | Save to DCIM on Android ≤ 9 only |
| `FOREGROUND_SERVICE` | Show download progress notification |
| `POST_NOTIFICATIONS` | Show completion/error notifications (Android 13+) |

---

## Limitations & notes

- **Private videos** cannot be downloaded (no login support)
- Facebook occasionally changes their page structure; if extraction stops working, the `parseVideoFromSource()` patterns in `FacebookVideoDownloader.kt` may need updating
- This app is for **personal use** of publicly shared content only — respect Facebook's Terms of Service
- The app does **not** require Facebook login

---

## Dependencies

| Library | Purpose |
|---------|---------|
| OkHttp 4.12 | HTTP requests |
| Jsoup 1.17 | HTML parsing (fallback) |
| Kotlin Coroutines 1.7 | Async download |
| AndroidX WorkManager | Background tasks |
| Material Components | UI |
