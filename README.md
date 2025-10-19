# CT526 - Simple-Web-using-Python-Flask
โปรเจกต์นี้เป็นตัวอย่างการพัฒนาเว็บแอปพลิเคชันด้วย **Flask (Python)**  
เพื่อศึกษาการใช้งาน `@app.route`, `templates`, และ `static` รวมถึงการนำค่าจากผู้ใช้มาประมวลผลด้วยฟังก์ชันจากไฟล์ภายนอก (`mylib.py`)  

เว็บไซต์นี้มีทั้งหมด **5 ส่วนหลัก** คือ  
- หน้าแนะนำสถานที่ท่องเที่ยว (`/`)  
- หน้าแสดงเทคโนโลยีที่สนใจ (`/tech`)  
- หน้าแสดงรหัสนักศึกษา (`/myid`)  
- หน้าแบบฟอร์มรับข้อมูลและผลลัพธ์ (`/draw`)  
- หน้าแสดงผลลัพธ์จากการรับข้อมูล (`/result`) 
---

```bash
# โครงสร้างของโปรเจกต์
├─ Simple-Web-using-Python-Flask
   ├── main.py                      # ไฟล์หลักของ Flask (กำหนด route แต่ละหน้า)
   ├── mylib.py                     # ไฟล์ฟังก์ชันที่ใช้คำนวณหรือประมวลผล (myfunc)
   ├── __pycache__
   │   └── mylib.cpython-313.pyc
   ├── README.md
   ├── static                       # เก็บไฟล์ภาพ
   │   ├── cloud.png
   │   ├── network.png
   │   └── samui.png
   └── templates                    # เก็บไฟล์ HTML (Template)
       ├── draw.html                # หน้า Input Form
       ├── result.html              # หน้าแสดงผลลัพธ์
       ├── tech.html                # หน้าเทคโนโลยีที่สนใจ
       └── tourist-site.html        # หน้าแนะนำสถานที่ท่องเที่ยว
```
---

**ขั้นตอนการสร้างเว็บด้วย Flask**
1. ติดตั้ง Flask
   ```bash
   pip install flask
   ```
2. สร้างไฟล์หลัก main.py
ใช้สำหรับกำหนด route ของแต่ละหน้า เช่น /, /tech, /myid, /draw

3. สร้างโฟลเดอร์ templates/
เก็บไฟล์ HTML เช่น tourist-site.html, tech.html, draw.html, result.html

4. สร้างโฟลเดอร์ static/
สำหรับเก็บรูปภาพหรือไฟล์อื่น ๆ เช่น samui.png, cloud.png

5. สร้างไฟล์ mylib.py
เก็บฟังก์ชันที่ใช้คำนวณหรือประมวลผล เช่น
   ```bash
    def myfunc(x, y):
    return x * y
   ```
6. เชื่อมโยง HTML กับ Flask ด้วย render_template()
และใช้ request.form รับค่าจากแบบฟอร์ม (POST)

7. เปิดเว็บ    
   (ถ้าไม่กำหนด port ต้องใส่ :5000)
   ```bash
    http://127.0.0.1/
   ```
   หรือ
    ```bash
    http://localhost/
   ```
   ---

**ขั้นตอนการรันด้วย Ubuntu**
1. อัปเดตข้อมูลแพ็กเกจทั้งหมดในระบบ Ubuntu
    ```bash
   sudo apt update
   ```

2. ติดตั้ง Python, pip, venv และ Git (เครื่องมือจำเป็น)
   ```bash
   sudo apt install python3 python3-pip python3-venv git -y
   ```

3. git clone และ cd ไปที่ Repository

4. สร้าง Virtual Environment (จำลอง Python)
   ```bash
   python3 -m venv venv
   ```

5. เปิดใช้งาน Virtual Environment
   ```bash
   source venv/bin/activate
   ```

6. ติดตั้ง Flask ภายใน Virtual Environment
   ```bash
   pip install flask
   ```

7. รันเว็บ
   ```bash 
   python3 main.py
   ```

8. เช็ค IP ของ Ubuntu VM
   ```bash
   ip addr
   ```

9. เปิดเว็บจากบน Host
   เอา IP ของ Ubuntu VM มาใส่บน Host 
   (ถ้าไม่กำหนด port ต้องใส่ :5000)
   ```bash
   http://192.168.x.x
   ```

