<h3 align="center">มหาวิทยามหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกําแพงแสน</h3>
<h5 align="center">คณะวิศวกรรมศาตร์ กำแพงแสน ภาควิชาวิศวกรรมคอมพิวเตอร์</h5>

# ITM Project: Reverse Image Search for Online Shopping
**:bulb: Project นี้เป็นส่วนหนึ่งของรายวิชา Management of Information Technology 02204372-60 :bulb:**

> ## :gear: การ setup Environment สำหรับโปรเจค :gear:
1. การลง library ที่ใช้ในการทำโปรเจค
    -
    -
2. ทำการ Clone ตัว Repository
3. การนำฐานข้อมูลลงในตัว XAMPP
    - ทำการสร้างฐานข้อมูลใน http://localhost/phpmyadmin/ ตั้งชื่อ database ว่า itm_database
    - import : file "itm_databaseVfinal.sql" ใน folder: Database

4. ทำการเปลี่ยน path ตามความต้องการใน file "app.py" *path ทั้งหมดต้องอยู่ใน folder: Flask_Run_Application*
5. ทำการ run file "app.py" ใน folder: Flask_Run_Appliction

> ## :man: สมาชิกภายในทีม :man:

| ชื่อ | หน้าที่ |
| ------------- | ------------- |
| นายธีรภัทร อักษรนันท์  | Frontend Developer |
| นายอาบิ๊ด มหากลั่น  | Web Design, Supporter |
| นายชนกานต์ ศรีศรุติพร  | Project Manager, Supporter |
| นายปวิช สังข์วารี  | AI Developer, Backend Developer |

> ## :checkered_flag: ลำดับการทำงาน :checkered_flag:

- [x] I. วางแผนการทำงานโครงการ
- [x] II. การออกแบบเว็บไซต์
- [x] III. การออกแบบฐานข้อมูล 
- [x] IV. สร้างฐานข้อมูล
- [x] V. พัฒนาโครงสร้างเว็บไซต์
- [x] VI. รวบรวม Dataset และ Pre-process
- [x] VII. Train Model AI / Evaluate 
- [x] VIII. นำ Model AI เข้าเว็บไซต์ 
- [x] IX. ทดสอบการทำงานโดยรวม **_(อยู่ในกระบวนการ)_** 

> ## :clipboard: รายละเอียดแต่ละงาน :clipboard:

##### _1 วางแผนการทำงานโครงการ_

| **_เทคโนโลยี หรือ ซอฟแวร์_** | **_ฟังก์ชัน_** | **_รายละเอียด_** |
| :-------------: | :-------------: | ------------- |
| ![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) | IDE | โปรแกรมประยุกต์ซอฟต์แวร์ที่ช่วยให้โปรแกรมเมอร์พัฒนาซอฟต์แวร์ได้อย่างมีประสิทธิภาพ ในที่นี่ใช้ในการทำทุกๆอย่าง |
| ![Xampp](https://img.shields.io/badge/Xampp-F37623?style=for-the-badge&logo=xampp&logoColor=white) | Frameworks & Library | XAMPP Version: 7.4.29 |
| ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) | Languages | ใช้สำหรับการ Coding ทั้งทางด้าน AI แล้วก็ Backend |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Frameworks & Library | Python Framework ช่วยให้การทำงานเป็นรูปแบบมายิ่งขึ้น ตามแนวทาง MVC |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Languages | ภาษาที่ใช้ในการทำโครงหน้าเว็บไซต์ |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Languages | ภาษาที่ใช้ในการตกแต่งหน้าเว็บให้มีความสวยงามมากยิ่งขึ้น |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white) | Frameworks & Library | เครื่องมือที่ใช้เขียนcodeในการที่เราจะสร้าง machine learning model |
| ![Conda](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white) | Frameworks & Library | Conda เป็นที่ setting Environment library ที่จำเป็นใน Python |
---
##### _2 การออกแบบเว็บไซต์_
Reference ในการจัดทำหน้าเว็บไซต์ (ไฟล์ : Reference_1, Reference_2 :file_folder: WebDesign)

<h5 align="center">[...Reference_1...]</h5>

![Reference_1](https://user-images.githubusercontent.com/75871892/218113513-9cc7d003-1f6f-476b-a31d-47d9908fe957.jpg)

<h5 align="center">[...Reference_2...]</h5>

![Reference_2](https://user-images.githubusercontent.com/75871892/218114005-c116e943-093d-4885-a98c-86efb21a2673.jpg)

:+1::+1::+1: [Credit Youtube](https://www.youtube.com/watch?v=P8YuWEkTeuE&list=LL&index=4&t=950s) BY [Tech2 etc](https://www.youtube.com/@Tech2etc)

จาก Reference ทำการออกแบบด้วย Figma (ไฟล์ : Design_[1-4] :file_folder: WebDesign) [[Web Figma]](https://www.figma.com/file/696OFGQbJxsx3QN6u3Ag4p/ITM-Web-design?node-id=0%3A1&t=E9WbLndiAib3A6ks-0)

<p align="center">
    <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"/>
</p>


![Design_1](https://user-images.githubusercontent.com/75871892/218508883-21a55009-2e40-4b59-8b29-f19e75d9dcce.jpg)

![Design_2](https://user-images.githubusercontent.com/75871892/218508859-822e0dae-21ac-4585-bc1b-51311cc7654f.jpg)

![Design_3](https://user-images.githubusercontent.com/75871892/218508867-14c4cd4e-da39-4155-a2f5-6916c2ab9927.jpg)

![Design_4](https://user-images.githubusercontent.com/75871892/218508878-99926ea1-63fe-46c0-ac98-407dcf878f8e.jpg)

![Design_5](https://user-images.githubusercontent.com/75871892/219263139-067d860a-86de-488b-9a1d-d26388b704e8.jpg)

<h5 align="center">[...Sign in | Sign up...]</h5>

![Design_SignIn](https://user-images.githubusercontent.com/75871892/221206698-2d13d472-ce9b-41d1-a809-4c08e58a5c83.jpg)

![Design_SignUp](https://user-images.githubusercontent.com/75871892/221206712-2883d9c2-42fa-46f9-a708-491d109bd846.jpg)


<h5 align="center">[...Admin...]</h5>

![Design_Admin_1](https://user-images.githubusercontent.com/75871892/219263569-259f7c78-8787-484e-a17c-bb45b3f9279a.jpg)

![Design_Admin_2](https://user-images.githubusercontent.com/75871892/219263572-833cc740-3b94-4953-a24d-ff5ba304a4cc.jpg)

![Design_Admin_3](https://user-images.githubusercontent.com/75871892/219263565-140f8487-71c1-4dbb-a31a-747358fe418b.jpg)

<h5 align="center">[...About Us...]</h5>

![Design_AboutUs_1](https://user-images.githubusercontent.com/125015450/222890431-dc3ca41d-0a78-443a-bc4e-e307516ac9ad.png)
![Design_AboutUs_2](https://user-images.githubusercontent.com/125015450/222890432-743fd287-eb48-4919-b28a-093eb8a7e485.png)
![Design_AboutUs_3](https://user-images.githubusercontent.com/125015450/222890429-e11114f3-d819-4064-9c86-b6fd4da411cf.png)



---
##### _3 การออกแบบฐานข้อมูล_
การออกแบบเป็นดังภาพที่เห็นต่อไปนี้ (ไฟล์ : ER_Diagram_1 / :file_folder: Picture_Document)

Prototype 1


![ER_Diagram_1](https://user-images.githubusercontent.com/75871892/218267022-5d726e8f-daaf-40b8-abbf-2faf8ad6c074.jpg)
<br>

Prototype 2

![ER_Diagram_2](https://user-images.githubusercontent.com/75871892/219260027-1fa77d80-f1dd-43c4-b436-b104b5bebe3b.jpg)

Prototype 3

![ER_Diagram_3](https://user-images.githubusercontent.com/75871892/221345499-b73526d5-31cd-4bc9-b7ef-470346545301.jpg)

---
##### _4 สร้างฐานข้อมูล_

Database (ไฟล์ : itm_database / :file_folder: Database/itm_database.sql) 


![SQL_Image](https://user-images.githubusercontent.com/75871892/218263682-1701a9fe-3509-4062-b6b3-f5b0caac6220.jpg)

![SQL_Image_2](https://user-images.githubusercontent.com/75871892/219265339-720c756f-f94a-4a83-9a9e-6072a95fcc9a.jpg)

![SQL_Image_3](https://user-images.githubusercontent.com/75871892/221345500-0450f072-0904-408e-9618-f6ec07eec9e6.jpg)


---
##### _5 พัฒนาโครงสร้างเว็บไซต์_
Code ของเว็บไซค์ อยู่ใน :file_folder: WebPrototype
<br>

![Web_1](https://user-images.githubusercontent.com/75871892/218263858-f6f43f39-2b27-4369-8fa7-da0d7e7ea03e.jpg)


<br>

![Web_2](https://user-images.githubusercontent.com/75871892/218321568-73f9cfbf-9291-4ffe-8fdc-6e49e1606ea0.jpg)

<br>

![Web_3](https://user-images.githubusercontent.com/75871892/218321558-994c2cfa-de8d-4f69-8ebc-695bb011b22d.jpg)

<br>

![Web_4](https://user-images.githubusercontent.com/75871892/218321565-a59973e6-2312-4ba8-b3c1-c8198e209537.jpg)

<br>

![Web_5](https://user-images.githubusercontent.com/75871892/219263802-65038732-fc59-43d5-8107-f29b2c9333ac.jpg)

<br>

![Web_6](https://user-images.githubusercontent.com/75871892/219263778-d39454d0-a9b3-44aa-baf0-d6678713b974.jpg)

<br>

![Web_7](https://user-images.githubusercontent.com/75871892/219263785-42921148-db69-4e06-9b2a-0e0fceb2bbbd.jpg)

<br>

![Web_8](https://user-images.githubusercontent.com/75871892/221364748-aa5dff43-8d1e-4606-aa13-69a9551d31d7.jpg)

<br>

![Web_9](https://user-images.githubusercontent.com/75871892/221364743-a2c63cd2-4b75-493d-b8b2-7d8a2959e5b1.jpg)

<br>

![Web_10](https://user-images.githubusercontent.com/75871892/221364745-a291654c-957c-45ce-a402-948ff83ef62e.jpg)


---
##### _6 รวบรวม Dataset และ Pre-process_
นำตัว Dataset ทั้งหมดมาจากตัวของ เว็บ kaggle

| **_Class_** | **_จำนวน_** | **_Source_** |
| :-------------: | :-------------: |  ------------- |
| **Shirt** | 1993 | [Shirt Dataset](https://www.kaggle.com/datasets/sunnykusawa/tshirts?resource=download) |
| **Shorts** | 3372 | [Shorts Dataset](https://www.kaggle.com/datasets/kritanjalijain/outfititems) |
| **Pants** | 2975 | [Pants Dataset](https://www.kaggle.com/datasets/kritanjalijain/outfititems) |
| **Skirt** | 2975 | [Skirt Dataset](https://www.kaggle.com/datasets/kritanjalijain/outfititems) |
| **Shoe** | 1000 | [Shoe Dataset](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images) |
| **Sandal** | 1000 | [Sandal Dataset](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images) |

---
##### _7 Train Model AI / Evaluate_

---
##### _8 นำ Model AI เข้าเว็บไซต์_
การใช้ flask ร่วมกัน keras ในการ Load model เข้ามาร่วมทำงาน

```python
model = keras.models.load_model('D:/ITM_Group4_Reverse_Image_Search_for_Online_Shopping/Model/preweight/efficientnet.h5', custom_objects={'KerasLayer': hub.KerasLayer})

model.summary()
```

ยังมี library อื่นๆที่เกี่ยวข้องอีกตามนี้
```python
from werkzeug.utils import secure_filename
import json
import pandas as pd
from scipy.spatial import distance
from PIL import Image
from tensorflow import keras
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
```
---
##### _9 ทดสอบการทำงานโดยรวม_

