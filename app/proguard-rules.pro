# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.

# Keep OkHttp classes
-dontwarn okhttp3.**
-keep class okhttp3.** { *; }
-keep interface okhttp3.** { *; }

# Keep Jsoup classes
-keep class org.jsoup.** { *; }

# Keep our downloader classes
-keep class com.fbdownloader.** { *; }

# Keep Kotlin coroutine classes
-keep class kotlinx.coroutines.** { *; }
-dontwarn kotlinx.coroutines.**

# Keep WorkManager
-keep class androidx.work.** { *; }
