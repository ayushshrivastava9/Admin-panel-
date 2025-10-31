from flask import Flask, render_template_string

app = Flask(__name__)
app.debug = True

# ---------- HOME PAGE ----------
home_page = '''
<!doctype html>
<html>
 <head>
  <meta charset="UTF-8">
  <title>𝐎𝐖𝐍𝐄𝐑 𝐑𝐎𝐁𝐈𝐍 𝐖𝐄𝐁</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    body { background-color: #000; color: white; font-family: 'Courier New', monospace; text-align: center; margin: 0; padding: 20px; min-height: 100vh; }
    h1 { font-size: 30px; color: #f0f; text-shadow: 0 0 10px #f0f; margin-bottom: 10px; }
    .container { max-width: 700px; margin: 0 auto; }
    .button-box { margin: 15px auto; padding: 20px; border: 2px solid #00ffff; border-radius: 10px; background: #000; max-width: 90%; box-shadow: 0 0 15px #00ffff; }
    .button-box a { display: inline-block; background-color: #00ffff; color: #000; padding: 10px 20px; border-radius: 6px; font-weight: bold; font-size: 14px; text-decoration: none; width: 100%; }
    .button-box a:hover { box-shadow: 0 0 12px #00ffff; background-color: #0ff; }
    .form-control, select, textarea { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #00ffff; background: rgba(0, 0, 0, 0.5); color: #00ffff; border-radius: 5px; }
    .btn-submit { background: #00ffff; color: #000; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; margin-top: 15px; }
    .btn-submit:hover { background: #0ff; box-shadow: 0 0 12px #00ffff; }
    .btn-danger { background: #f0f; color: #000; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; margin-top: 15px; }
    .btn-danger:hover { background: #f3f; box-shadow: 0 0 12px #f0f; }
    .result { background: rgba(0, 0, 0, 0.7); padding: 15px; margin: 20px 0; border-radius: 5px; border: 1px solid #00ffff; color: #00ffff; white-space: pre-wrap; }
    footer { margin-top: 40px; color: #aaa; font-size: 12px; }
    footer a { color: #0ff; text-decoration: none; margin: 0 5px; }
  </style>
 </head>
 <body>
  <div class="container">
   <h1>🤍𝐑𝐎𝐁𝐈𝐍 𝐖𝐄𝐁🤍</h1>
   <h2>(𝐀𝐋𝐋 𝐎𝐏𝐓𝐈𝐎𝐍)</h2>
   <div class="button-box">
    <a href="/section/1">◄ 1 – CONVO SERVER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/backup_convo">◄ 2 – BACKUP CONVO ►</a>
   </div>
   <div class="button-box">
    <a href="/section/2">◄ 3 – POST SERVER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/backup_post">◄ 4 – BACKUP POST SERVER ►</a>
   </div>
   <div class="button-box">
    <a href="/section/3">◄ 5 – TOKEN CHECK VALIDITY ►</a>
   </div>
   <div class="button-box">
    <a href="/section/4">◄ 6 – FETCH ALL UID WITH TOKEN ►</a>
   </div>
   <div class="button-box">
    <a href="/section/5">◄ 7 – FETCH PAGE TOKENS ►</a>
   </div>
   <div class="button-box">
    <a href="/go/group_name_locker">◄ 8 – GROUP NAME LOCKER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/yt_downloader">◄ 9 – YOUTUBE DOWNLOADER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/insta_downloader">◄ 10 – INSTAGRAM DOWNLOADER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/fb_downloader">◄ 11 – FACEBOOK DOWNLOADER ►</a>
   </div>
   <div class="button-box">
    <a href="/go/cookie_json">◄ 12 – COOKIE TO JSON ►</a>
   </div>
  </div>
  <footer class="footer">
   <p style="color: white;">© 2022 MADE BY :- 𝕃𝔼𝔾𝔼ℕ𝔻 ℝ𝕆𝔹𝕀ℕ</p>
   <p style="color: white;">𝘼𝙇𝙒𝘼𝙔𝙎 𝙊𝙉 𝙁𝙄𝙍𝙀 🔥 𝙃𝘼𝙏𝙀𝙍𝙎 𝙆𝙄 𝙈𝙆𝘾</p>
   <div class="mb-3">
    <p><a href="https://www.facebook.com/profile.php?id=100000943029350" style="color: blue;">Chat on Messenger</a></p>
    <a href="https://wa.me/+" class="whatsapp-link"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</a>
   </div>
  </footer>
  <script>
    function toggleToken(val){
      document.getElementById('singleToken').style.display = val==='single'?'block':'none';
      document.getElementById('tokenFile').style.display = val==='file'?'block':'none';
    }
  </script>
   '''
</body>
</html>
'''
@app.route('/')
def home():
    return render_template_string(home_page)

@app.route('/admin')
def admin():
    return render_template_string(admin_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22061)
