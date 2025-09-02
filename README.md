# RS Earning Bot (Firebase + GitHub Pages)

🚀 A simple earning app built with **Firebase Auth + Firestore** and hosted free on **GitHub Pages**.

---

## 🔥 Features
- Google Login + Email/Password Login (Firebase Auth)
- Firestore integration for user data (coins, profile, leaderboard)
- Home page → Claim ads and earn coins
- Wallet → Live balance + withdraw option
- Leaderboard → Top users in real-time
- Profile → Name, photo, email, coins live
- Refer → UID / Referral link copy & share

---

## 📦 How to Deploy on GitHub Pages

### 1. Create GitHub Repo
1. Login to GitHub → Create a new repository (public)
2. Name it: `RS-earning-bot`
3. Do NOT add template files (keep empty)

### 2. Upload Files
1. Upload your HTML (`index.html`) → This must be renamed from `RS_GitHubReady.HTML`
2. (Optional) Upload README.md and other assets

### 3. Enable GitHub Pages
1. Go to Repository → Settings → Pages
2. Source → Select `Branch: main` → `/ (root)`
3. Save ✅

### 4. Your Live App
After a few minutes your app will be live at:
```
https://your-username.github.io/RS-earning-bot/
```

---

## ⚠️ Notes
- Make sure to add your **Firebase config keys** inside `index.html`
- Firestore security rules must allow read/write for testing
- Later, lock rules properly for production

---

👨‍💻 Made for mobile hosting without PC (GitHub Pages + Firebase)
