<h3 align="center">มหาวิทยามหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกําแพงแสน</h3>
<h5 align="center">คณะวิศวกรรมศาตร์ กำแพงแสน ภาควิชาวิศวกรรมคอมพิวเตอร์</h5>

# ITM Project: Reverse Image Search for Online Shopping
**:bulb: Project นี้เป็นส่วนหนึ่งของรายวิชา Management of Information Technology 02204372-60 :bulb:**

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
- [ ] VI. รวบรวม Dataset และ Pre-process
- [ ] VII. Train Model AI / Evaluate
- [ ] VIII. นำ Model AI เข้าเว็บไซต์ 
- [ ] IX. ทดสอบการทำงานโดยรวม 

> ## :clipboard: รายละเอียดแต่ละงาน :clipboard:

##### _1 วางแผนการทำงานโครงการ_

| เทคโนโลยี หรือ ซอฟแวร์ | ฟังก์ชัน | รายละเอียด |
| :-------------: | :-------------: | ------------- |
| ![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) | IDE | # |
| ![Xampp](https://img.shields.io/badge/Xampp-F37623?style=for-the-badge&logo=xampp&logoColor=white) | Frameworks & Library | XAMPP Version: 7.4.29 |
| ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) | Languages | ใช้สำหรับการ Coding ทั้งทางด้าน AI แล้วก็ Backend |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Frameworks & Library | Python Framework ช่วยให้การทำงานเป็นรูปแบบมายิ่งขึ้น ตามแนวทาง MVC |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Languages | ภาษาที่ใช้ในการทำโครงหน้าเว็บไซต์ |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Languages | ภาษาที่ใช้ในการตกแต่งหน้าเว็บให้มีความสวยงามมากยิ่งขึ้น |

---
##### _2 การออกแบบเว็บไซต์_
Reference ในการจัดทำหน้าเว็บไซต์ (ไฟล์ : Reference_1, Reference_2 :file_folder: WebDesign)

<h5 align="center">[...Reference_1...]</h5>

![Reference_1](https://user-images.githubusercontent.com/75871892/218113513-9cc7d003-1f6f-476b-a31d-47d9908fe957.jpg)

<h5 align="center">[...Reference_2...]</h5>

![Reference_2](https://user-images.githubusercontent.com/75871892/218114005-c116e943-093d-4885-a98c-86efb21a2673.jpg)

:+1::+1::+1: [Credit Youtube](https://www.youtube.com/watch?v=P8YuWEkTeuE&list=LL&index=4&t=950s) BY [Tech2 etc](https://www.youtube.com/@Tech2etc)

จาก Reference ทำการออกแบบด้วย Figma (ไฟล์ : Design_[1-4] :file_folder: WebDesign)

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=figma" />
  </a>
</p>

![Design_1](https://user-images.githubusercontent.com/75871892/218508883-21a55009-2e40-4b59-8b29-f19e75d9dcce.jpg)

![Design_2](https://user-images.githubusercontent.com/75871892/218508859-822e0dae-21ac-4585-bc1b-51311cc7654f.jpg)

![Design_3](https://user-images.githubusercontent.com/75871892/218508867-14c4cd4e-da39-4155-a2f5-6916c2ab9927.jpg)

![Design_4](https://user-images.githubusercontent.com/75871892/218508878-99926ea1-63fe-46c0-ac98-407dcf878f8e.jpg)

---
##### _3 การออกแบบฐานข้อมูล_
การออกแบบเป็นดังภาพที่เห็นต่อไปนี้ (ไฟล์ : ER_Diagram_1 / :file_folder: Picture_Document)

Prototype 1


![ER_Diagram_1](https://user-images.githubusercontent.com/75871892/218267022-5d726e8f-daaf-40b8-abbf-2faf8ad6c074.jpg)
<br>

---
##### _4 สร้างฐานข้อมูล_

Database (ไฟล์ : itm_test_database / :file_folder: Database/itm_test_database.sql 


![SQL_Image](https://user-images.githubusercontent.com/75871892/218263682-1701a9fe-3509-4062-b6b3-f5b0caac6220.jpg)

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
