# Pwn - Gemaa

## Deskripsi
Gemaa adalah soal yang membutuhkan _netcat service_. Jalankan file `files/gema` yang merupakan hasil kompilasi dari `files/gema.cpp` sehingga dapat diakses dengan menggunakan `netcat` melalui jaringan di luar container. Anda dapat menggunakan `socat` atau program lain yang Anda ketahui.

_Service_ dinyatakan berhasil dipasang apabila saat dilakukan `nc <IP SERVER> <MACHINE PORT>` (Windows: `netcat <IP SERVER> <MACHINE PORT>`) akan mengembalikan respon berikut:
```
WELCOME WELCome Welcome welcome...
Enter 'exit' if you want to exit.
>>
```

## Spesifikasi Dockerfile
- OS: Ubuntu 18.04
- User: compfest15
- Container port: 4321
- Working directory: /home/compfest15
- Gunakan container port sebagai listening port untuk `socat` atau program sejenis

## Spesifikasi docker-compose.yml
- Compatible dengan docker engine versi 19 ke atas.
- Lakukan mapping port dari container ke host (server/komputer Anda) sesuai dengan machine port. Machine port adalah `1[4 digit terakhir NPM Anda]`, e.g. Misal NPM saya 1234567890, maka machine port saya adalah `17890`.
- Nama container gunakan `PWN_[NPM]` sebagai contoh `PWN_1234567890`.
- Lakukan setting agar container melakukan restart hanya saat terjadi kegagalan.

## Referensi
- [Netcat](https://en.wikipedia.org/wiki/Netcat)
- [Socat](https://www.redhat.com/sysadmin/getting-started-socat)
