<img width="257" height="308" alt="image" src="https://github.com/user-attachments/assets/95f84a6b-9b6a-4028-bdb7-40b2b4ba630d" />
ini adalah hasil dari run program saya

<img width="469" height="344" alt="image" src="https://github.com/user-attachments/assets/01cb789a-9dc6-4ef7-b808-10298c585024" />
ini isi dari file json yang berisikan data agar bisa di panggil di py, awalnya hanya berisi 2 orang. Tapi karena tadi saya sudah panggil 2 orang lagi jadinya datanya bertabah jadi 4 begitu pun seterusnya kalau terjadi penambahan data.



<img width="130" height="27" alt="image" src="https://github.com/user-attachments/assets/5afdffd8-6c50-4b0e-92b3-58302a924f2b" />
import json
- Memanggil library JSON.
- Digunakan untuk membaca (load) dan menyimpan (dump) data dalam format JSON.
from pathlib import Path
- Mengambil fungsi Path untuk mengatur lokasi file.
- Membantu program mencari file tanpa harus menulis alamat folder secara manual.

<img width="273" height="84" alt="image" src="https://github.com/user-attachments/assets/150363a2-6962-498e-8bca-e19900e40862" />
untuk membuat alamat file bernama JSON SC 6.json yang berada dalam folder yang sama dengan file program Python. __file__ digunakan untuk mengetahui lokasi file Python yang sedang dijalankan, kemudian .parent mengambil lokasi foldernya.
Program menggunakan blok try-except untuk menangani kemungkinan kesalahan saat membuka file. Pada bagian try, program mencoba membuka file JSON menggunakan fungsi open() dengan mode "r" yang berarti membaca file. Setelah file terbuka, fungsi json.load() digunakan untuk mengambil isi file JSON dan mengubahnya menjadi bentuk data Python agar dapat diproses.

<img width="302" height="337" alt="image" src="https://github.com/user-attachments/assets/c20fb336-62fd-4a39-ba8c-8c9a25f7be73" />
Program dibuat menggunakan perulangan while True agar menu terus muncul sampai pengguna memilih keluar. Pada awalnya program menampilkan tiga pilihan, yaitu melihat nilai, menambah nilai, atau keluar. Pilihan pengguna kemudian disimpan dalam variabel pilihan untuk menentukan proses yang akan dijalankan.
Jika pengguna memilih menu 1, program akan menampilkan data nilai mahasiswa yang sudah tersimpan. Program terlebih dahulu mengecek apakah variabel data berisi data atau masih kosong menggunakan if not data. Jika belum ada data, program memberikan informasi bahwa data belum tersedia. Namun, jika terdapat data, perulangan for m in data akan membaca setiap data mahasiswa satu per satu, kemudian menampilkan informasi berupa NIM, nama, mata kuliah, dan nilai menggunakan format f-string agar tampilan lebih rapi.
Jika pengguna memilih menu 2, program akan menjalankan proses input data mahasiswa baru. Pengguna diminta memasukkan NIM, nama, dan mata kuliah. Fungsi .strip() digunakan untuk menghapus spasi yang tidak diperlukan pada input sehingga data yang tersimpan lebih bersih. Setelah itu program melakukan pengecekan menggunakan kondisi if not nim or not nama or not matkul untuk memastikan seluruh identitas mahasiswa telah diisi. Apabila ada bagian yang kosong, program akan memberikan pesan kesalahan dan menjalankan continue agar kembali ke menu awal.

<img width="250" height="204" alt="image" src="https://github.com/user-attachments/assets/0eb097a7-8c4e-46b6-a6d8-7afc76db6d35" />
jelaskan kode ini
Kode pada bagian ini merupakan proses akhir setelah data mahasiswa berhasil divalidasi, yaitu menambahkan data baru ke dalam penyimpanan sementara, menyimpan data tersebut ke file JSON, serta mengatur pilihan keluar dari program.
