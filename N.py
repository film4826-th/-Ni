from flask import Flask
import os

app = Flask(__name__)

# 📌 ฟังก์ชันอ่านค่าจำนวนดาวน์โหลด
def read_counter():
    if not os.path.exists("counter.txt"):
        with open("counter.txt", "w") as f:
            f.write("0")
    with open("counter.txt", "r") as f:
        return int(f.read().strip())

# 📌 ฟังก์ชันเพิ่มจำนวนดาวน์โหลด
def increment_counter():
    count = read_counter() + 1
    with open("counter.txt", "w") as f:
        f.write(str(count))
    return count

# 📌 หน้าแรก: ให้กดไป YouTube
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>ติดตาม YouTube ก่อน</title>
        <script>
            function goToYouTube() {
                window.open("https://www.youtube.com/@krchannel5578", "_blank"); // ✅ เปลี่ยนเป็นลิงก์ช่องจริง
                setTimeout(function() { window.location.href = "/download"; }, 5000); // รอ 5 วิ แล้วไปหน้าดาวน์โหลด
            }
        </script>
        <style>
            @keyframes rainbow {
                0% { background-color: red; }
                16% { background-color: orange; }
                33% { background-color: yellow; }
                50% { background-color: green; }
                66% { background-color: blue; }
                83% { background-color: indigo; }
                100% { background-color: violet; }
            }
            body {
                font-family: Arial, sans-serif; text-align: center; 
                background: url('https://cdn.discordapp.com/attachments/1319648931457667093/1335831637371519029/Screenshot_765_2.png?ex=67a199a8&is=67a04828&hm=6beff69ffe93d0ee0476b97b50fb66b78a8d092fa6b3f24e6b6c9828a446be38&')no-repeat center center fixed; 
                background-size: cover; color: white; padding: 50px;
            }
            .container { 
                max-width: 600px; margin: auto; background: rgba(0, 0, 0, 0.7); 
                padding: 20px; border-radius: 10px; 
            }
            h1 { color: #ffcc00; }
            .btn { 
                display: inline-block; padding: 10px 20px; margin: 10px; 
                color: white; border: none; border-radius: 5px; cursor: pointer; 
                font-size: 18px; text-decoration: none; 
                animation: rainbow 3s infinite; /* ทำให้เปลี่ยนสีวนลูป */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>กรุณาติดตามช่อง YouTube ก่อน</h1>
            <p>กดปุ่มด้านล่างเพื่อไปที่ช่อง YouTube ของเรา</p>
            <button class="btn" onclick="goToYouTube()">🔴 ไปที่ YouTube</button>
            <p>ระบบจะพาคุณไปหน้าดาวน์โหลดอัตโนมัติหลังจาก กดติดตามช่องเรา</p>
        </div>
    </body>
    </html>
    """

# 📌 หน้าดาวน์โหลด
@app.route('/download')
def download():
    count = increment_counter()  # เพิ่มจำนวนดาวน์โหลด
    return f"""
    <html>
    <head>
        <title>ดาวน์โหลดไฟล์</title>
        <style>
            @keyframes rainbow {{
                0% {{ background-color: red; }}
                16% {{ background-color: orange; }}
                33% {{ background-color: yellow; }}
                50% {{ background-color: green; }}
                66% {{ background-color: blue; }}
                83% {{ background-color: indigo; }}
                100% {{ background-color: violet; }}
            }}
            body {{
                font-family: Arial, sans-serif; text-align: center; 
                background: url('https://source.unsplash.com/1600x900/?space') no-repeat center center fixed; 
                background-size: cover; color: white; padding: 50px;
            }}
            .container {{ 
                max-width: 600px; margin: auto; background: rgba(0, 0, 0, 0.7); 
                padding: 20px; border-radius: 10px; 
            }}
            h1 {{ color: #ffcc00; }}
            .btn {{ 
                display: inline-block; padding: 10px 20px; margin: 10px; 
                color: white; border: none; border-radius: 5px; cursor: pointer; 
                font-size: 18px; text-decoration: none; 
                animation: rainbow 3s infinite;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ดาวน์โหลด ENB.V2</h1>
            <p>ขอบคุณที่ติดตาม! กดปุ่มด้านล่างเพื่อดาวน์โหลด</p>
            <a class="btn" href="https://drive.google.com/uc?export=download&id=1-nn1KIyTeEmdI0AYuEwYz_Gb-7ihYlfj">⬇️ ดาวน์โหลดไฟล์</a>
            <p><strong>จำนวนดาวน์โหลดทั้งหมด:</strong> {count} ครั้ง</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
