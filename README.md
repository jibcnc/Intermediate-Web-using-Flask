# CT526-Intermidiate-Web-Using-Flask

1. เปิดให้เว็บสามารถเข้าถึงได้จาก Host ใดก็ได้
```bash
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
```
จะสามารถเข้าผ่าน IP ของเครื่องได้ เช่น
http://192.168.1.127 หรือ http://127.0.0.1 หรือ localhost

---

2. เพิ่ม route ไปที่ "/sum/xx/yy"     
สำหรับการเอาค่า xx , yy ที่ใส่มาบวกกัน
```bash
@app.route('/sum/<xx>/<yy>')
```

ตัวอย่างถ้าใส่ค่าถูกต้อง
```bash
http://192.168.1.127/sum/10/5
```

จะแสดงผล
```bash
The result of sum between 10 and 5 is 15
```

ตัวอย่างถ้าใส่ค่าผิด
```bash
http://192.168.1.127/sum/x/y
```

จะแสดงผล
```bash
You are using miss data type for operation
```

---

3. เพิ่ม route ไปที่ "/concat/xx/yy"  
สำหรับการเอาค่า xx , yy ที่ใส่มาต่อกัน
```bash
@app.route('/concat/<xx>/<yy>')
```

ตัวอย่าง
```bash
http://192.168.1.127/sum/10/5
```

จะแสดงผล
```bash
The result of concatenate between 10 and 5 is 105
```