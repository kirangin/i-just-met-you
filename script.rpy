define a  = Character("Arda")
define b  = Character("Bibi")
define h  = Character("Harris")
define m  = Character("Michael")
define p2 = Character("Perempuan")
define k  = Character("Karina")

define ac = Character("Arda (Chat)")
define kc = Character("Karina (Chat)")
define i  = Character("Ibu")

# Unknown/Other characters
define u  = Character("???")
define p  = Character("Penumpang")
define t  = Character("Tetangga")

# Kombinasi
define am = Character("Arda & Michael")

label start:
  scene bg dalam_kereta

  "Tuttt! Tuttt! Tuttt!"

  "Suara kereta api yang aku naiki pun berbunyi dan rodanya mulai berputar." 
  "Aku berdiri di dalam gerbong D, dengan tas ransel yang aku bawa di punggungku." 
  "Kakek dan nenekku melambaikan tangannya ke arahku dari kejauhan, "
  "dengan senyuman yang mampu menghangatkan hati yang dingin ini,"
  "Aku mencoba untuk mendekati jendela yg terdekat"

  a "Permisi"

  "Ucapku pada orang yg sedang menduduki kursi D-4 tanpa wajah berdosa sambil mendekati jendela kursi D-4"
  "Aku melambaikan tanganku ke arah kakek & nenekku berdiri, aku bisa melihat senyuman mereka."
  "Mereka tampak bahagia setelah aku melambaikan tanganku kepada mereka."

  a "Bahagia itu... ternyata cukup sederhana..."

  "Kebahagiaan yang kudapatkan di dunia ini..."

  a "Ah?! M-maaf jika saya mengganggu, saya hanya ingin melambai balik kepada kakek & nenek saya di luar sana."
  p "Oh, gak apa-apa kok"
  a "Maaf-- permisi"

  "Aku keluar dari kursi penumpang itu dengan rasa malu"
  "Pheeew... beruntung sekali penumpang itu cukup baik, bagaimana jika aku berhadapan dengan penumpang yang gak kaleman ya?"

  a "Ergh..."

  "Mungkin aku sudah dimaki-maki..."
  "Aku mulai mencari kursi yang tercantum dari tiket yang baru saja kubeli"

  a "D-11, di mana ya D-11?"

  "Aku bergumam sambil melangkahkan kakiku mendekati kursiku"

  "Di samping kananku tertera D-11 pada dinding-dinding kereta api"

  a "Sip"

  "Di tempat dudukku, aku mulai memeriksa kembali barang bawaanku,"
  "walaupun aku yakin sudah membawa semuanya saat berada di rumah kakek dan nenekku"

  a "Baju dan celana aku bawa empat setel kalau gak salah..."

  "Rasa gelisah mulai menyelimutiku, "
  "Seakan-akan aku melupakan sesuatu yang seharusnya ada di dalam tas ranselku"

  a "Bentar..."
  a "(SATU SETEL LAGI KEMANAAAAA???!!!)"

  "Batinku mulai menjerit-jerit karena aku lupa membawa satu setel pakaianku"

  a "(SIAL SIAL SIAL SIAL!!!!! BAGAIMANA INI???!!!)"

  "Saking paniknya, aku mulai memeriksa baju yang ketinggalan dengan menyentuh pakaian yang vsedang aku pakai"


  "Sehingga aku sadar, baju yang aku pakai adalah satu setel pakaianku yang hilang"

  a "Hahhh... bodoh banget aku..."

  "Aku menghela nafasku karena sedikitnya kegiatan yang bisa aku lakukan di kereta api ini"
  "Cukup aneh"
  "Karena diri ini sudah terbiasa dengan berbaring di kasur dan melihat layar HP hingga berjam-jam"

  "Dengan banyaknya waktu luang, aku pun mencoba untuk menghitung seberapa banyak waktu yg dibutuh untuk tiba ke kota tujuanku"

  "(Kayaknya cukup 2 jam juga buat tidur, 1 jamnya tinggal main hp saja, aku juga bisa mengabari keluargaku atau apalah itu)"

  p2 "Permisi"
  a "Iya"

  "Aku kira kursi di depanku akan kosong selama perjalanan. "
  "Sial sekali, aku jadi harus lebih siaga kalau seperti ini"


  p2 "Tujuannya kemana kalau boleh tahu?"
  a "Ke Ciruka"

  "Kenapa dia harus bertanya? Untuk menunjukan kesopanan? Kebersamaan? Terlihat baik? Ramah?"

  p2 "Oh, tujuan kita sama dong"
  a "Hahaha, bisa begitu..."

  "Tetap saja aku menjawab pertanyaan dia"

  p2 "..."
  a "..."
  p2 "..."
  a "..."
  p2 "..."
  a "..."

  "Seperti itu saja?"
  "Apakah kau tidak ingin membicarakan hal lain?" 
  "Bukankah ini aneh?" 
  "Dia tiba-tiba menanyakan tujuanku, setelah aku jawab, dia langsung memainkan HP-nya"

  "Apa yang dia inginkan?"
  "Haruskah aku yang memulai perbincangannya?"
  "Halo, namaku Arda. Senang berjumpa denganmu sayang"
  "Tidak, tidak, tidak... apa yang aku pikirkan..."
  "Aku harus mulai darimana?"

  menu:
    "Ern...":
      jump true_end

    "...":
      jump bad_end

    "Halo":
      jump good_end

  return


label true_end:
  "Ya, tidak ada salahnya aku bertanya balik kepadanya"
  "Dengan basa-basi, artinya aku menunjukan bahwa aku orang yang baik. Seperti dia sebelumnya…."
  "Iya….kan?"

  a "Erm..."
  p "Ya?"
  a "(Aduh, aku harus mulai darimana?!)"
  p "N-namanya siapa?"

  "Hebat Arda... "
  "Anda baru saja menanyakan nama seseorang tanpa percakapan basa-basi agar orang itu merasa nyaman untuk menjawabnya..."

  p "Namaku? Nama aku Karina Halth! Nama kamu?"

  "Perempuan ini... Dia memberitahu nama lengkapnya tanpa rasa ragu!"
  
  a "Arda..."
  k "Arda...?"
  a "Ardavelt Donivier"
  k "Uwahhh, kayak nama keluarga kerajaan!"
  a "Sebenarnya memang nama keluarga kerajaan, hanya saja kami lebih memilih untuk hidup sederhana."

  "Hahaha... "
  "Keluarga kerajaan... "
  "Memang benar kami keluarga kerajaan, dan juga generasi terakhir. "
  "Ini semua karena si tua bangka sialan itu yang meninggalkan kami dengan hutang sebesar gunung Krakatau!"
  "Alhasil kami harus membayar hutang-hutangnya dengan harta kami, dan sisa harta yang kami memiliki saat itu hampir mencapai angka 0..."
  "{b} SIALAN KAU TUA BANGKA SIALAN!!! {/b}"
  "{b} JIKA AKU BISA KEMBALI KE MASA LALU,  {/b}"
  "{b} KU AKAN MENJADI BIDAN DISAAT KAU LAHIR, DAN MENEPUK PANTATMU SAMPAI KAU TIDAK BISA MENANGIS SELAMANYA KARENA KEHABISAN AIR MATA!!! {/b}"

  k "Ardaaa... yuhuuu..."
  a "Y-ya?"
  k "Kamu malah tiba-tiba bengong ngeliatin aku"
  a "Ah... maaf..."
  k "Ada apa? Apa aku secantik itu dimata kamu sampai-sampai bisa membuatmu bengong ngeliatin aku, whehehe..."
  a "Ah... bukan begitu! Aku--"
  k "Hahahahaha, aku bercanda, aku bercanda"

  "Perempuan ini cukup agresif, mungkin sangat agresif jika aku bisa menjadi pasangannya"

  "He--hehe... hehehehehe..."

  k "Kamu barusan bilang, kalau keluargamu berkehidupan sederhanakan?"
  a "Ya?"
  k "Apa benar sesederhana ini?"
  a "!"

  "Ini perempuan kalau ngomong mulutnya gak bisa dijaga sedikit apa?!"

  a "Y-ya... hahaha..."
  k "Hohhh... keren dong. Jarang-jarang ada anggota kerajaan yang mau hidup rendahan"

  "Breng--"

  k "Jadi kita bisa temenan dong!"
  a "Huh?"

  "Kenapa dia tiba-tiba ingin berteman denganku?"

  a "Kamu? Mau berteman denganku?"
  k "Hm! Hm!"

  "Dia mengangguk-ngangguk kepalanya dengan girang"
  "Seperti video anjing lucu yang aku tonton akhir-akhir ini di Yucub, sebuah platform untuk mengupload dan menonton video di internet"

  a "Kenapa kau ingin berteman denganku? Padahal kita baru saja bertemu karena sebuah ketidaksengajaan..."
  k "Ketidaksengajaan itu artinya sebuah takdir! Dan juga tidak ada salahnya kan untuk berteman dengan orang yang membuatmu nyaman?"

  "Ya, memang tidak ada salahnya..."
  "Tapi, apa dia tidak berpikir dua kali sebelum berteman dengan orang yang baru saja dikenal?"
  "Bagaimana dia mempunyai energi positif sebesar ini?"

  a "Ya... aku pikir aku bisa berteman denganmu"
  
  "Tidak ada salahnya jugakan untuk berteman?"

  k "YES! TEMAN PERTAMAKU DARI KOTA CIRUKA!"
  a "Karina! Shhhhh..."

  "Banyak orang mengarahkan mata mereka pada kami karena terlalu berisik." 
  "Bahkan di antara mereka ada yang berbisik, apa yang mereka bisikan..."

  k "Oh! M-maaf... hehehe..."
  a "Hahhh..."


  "Aku menghela nafasku, karena dilihat oleh beberapa orang cukup menguras mentalku"
  "Karena biasanya aku tidak pernah menjadi pusat perhatian, dan juga aku selalu menyendiri"
  "Mungkin aku harus lebih sering berinteraksi dengan orang yang berada di dekatku setiap harinya"

  k "Jadi, biasanya kamu ngapain aja kalau lagi senggang? Dari sudut pandang anak kerajaan nih, hehehe"
  a "Tentu saja seperti kebanyakan orang, berbaring di kasur, bermain HP, memainkan gameku yang ada di HP"

  "Memangnya apa lagi yang bisa kulakukan, hehehe..."

  k "Ehhh... kamu gak keluar rumah buat pergi ke hotel bintang lima?"
  a "Huh? Buat apa?"
  k "Bukannya kebanyakan orang kaya pergi ke hotel bintang lima buat bersantai-santai ya?"
  a "Hotel... bintang lima...?"
  k "Oh! oh! oh! Pasti ke pantai kan? Atau ke pulau pribadi! Ya kan?!"

  "Tunggu sebentar," 
  "Apakah dia pikir semua keluarga kerajaan akan selalu pergi liburan ke tempat yang sangat mewah?"

  a "Karina... sebenarnya--"
  k "Hm!"

  "Wajahnya penuh dengan ekspetasi yang tinggi, sangat menggemaskan!!"
  "AKU TIDAK INGIN WAJAH MENGGEMASKANNYA HILANG SEKARANG!!!"
  "ARGHHHHH!!! TAPI AKU HARUS BERKATA YANG SEBENARNYA!!!"

  a "Karina... "
  a "Gak semua keluarga kerajaan bisa liburan semewah itu. "
  a "Terakhir kali kami liburan semewah itu saat aku masih bayi, dan itu juga kami pergi ke tempat ayahnya kakekku, bukan ke tempat yang kami dambakan..."
  k "Ohhh..."

  "Memangnya apa yang dia harapkan dari keluarga kerajaan yang kere.…"

  k "Selain itu?"

  "Masih mau lanjut..."

  a "Aku juga sering memainkan PS3 bersama adikku di kamarnya"
  k "Hohhh... sepertinya kalian sangat dekat"
  a "Siapa?"
  k "Tentu saja kamu dan adikmu..."
  a "Oh..."

  "Bodohhh... kenapa aku sangat lemot"

  k "Pfffttt... Hahahahaha! K-kau lucu sekali! Hahahahaha!"
  a "Hehe... Hehehehe... Hahahahaha!"

  "Kami tertawa terbahak-bahak"

  "Aku tidak tahu kenapa kami berdua tertawa, mungkinkah karena lemotnya diriku, atau karena aku memang sangat lucu dimatanya"
  "Yang aku tahu hanyalah, aku dan dia tertawa"
  "Aku bahkan tidak peduli apa yang membuat dia tertawa, tapi rasanya melihat dia tertawa seperti ini membuatku sangat senang"
  "Aku ingin memulai perbincangan baru dengannya"
  "Hal apa lagi yang harus kita obrolkan, ya?"

  menu: 
    "Tentang dirinya":
      jump good_scene2

    "Tentang keluarganya":
      jump good_scene2

    "Tentang tujuannya ke Ciruka":
      jump good_scene2

  return 

label good_scene2:

  a "Kita kan sudah ngobrol tentang keluargaku, ada bagusnya kamu menceritakan tentang keluargamu juga, hehehe"
  k "..."
  a "Karina...?"
  k "..."

  "Apa yang terjadi?"
  "Apakah aku melakukan kesalahan? Apakah kata yang kulontarkan menyakiti perasaannya?"
  "Keluarganya..." 
  "Apakah dia memiliki masalah dengan keluarganya?"

  a "Karin--"
  k "Ya?"

  "Aku kaget setelah dia menjawab seruanku secepat itu"

  a "Tentang sebelumnya... aku mi--"
  k "Aku pergi ke Ciruka buat sekolah di sana kok. Di sana aku tinggal bersama nenekku!"
  k "Dia sangat baik, kadang-kadang dia memberikan aku sangat banyak uang jajan!"
  a "Ohh! Bagus dong kalau begitu!"
  k "Iya, hehehe"

  "Dia tinggal dengan neneknya..."
  "Apakah dia memiliki masalah dengan Ibu dan Ayahnya di kota sebelumnya..."
  "Aku tidak ingin terlalu memikirkannya," 
  "Aku harus membuat suasana yang baik dengan melanjutkan oborolan ini"

  a "Oh iya. Kamu kan ngomong kalau bakal sekolah di sini, tepatnya sekolah dimana?"
  k "SMAN 1 Ciruka"
  a "SMAN apa?"
  k "SMAN 1 Ciruka"

  "Sebentar, apakah aku tidak salah dengar?"
  "Dia akan sekolah di sana?"
  "Tempat di mana aku bersekolah?!"

  a "Karina..."
  k "Ya?"
  a "Artinya kau adalah teman sekolahku juga"
  k "Huh?"
  a "Teman..."
  a "Satu..."
  a "Sekolah..."
  a "Bersama..."
  a "Dengan..."
  a "Aku..."
  k "?"

  "Erghh, sepertinya dia memiliki processor yang jadul"

  k "!"
  k "Kamu..."
  k "Teman..."
  k "Satu..."
  k "Sekolah..."
  k "Bersama..."
  k "Dengan..."
  k "Aku..."

  a "Hm!"

  "Aku menganggukan kepalaku sambil tersenyum, mungkin kali ini dia akan mengerti"

  k "YES! AKU PUNYA TEMAN SATU SEKOLAH AKHIRNYA!"
  a "Shhh..."

  "Lagi, para penumpang di gerbong D mengarahkan perhatian mereka pada kami dengan berbagai varian perasaan, risih, penasaran, marah, dan lain-lain"

  k "M-maaf, hehehe..."
  k "Artinya kita sekelas dong?!"
  a "Ya enggak juga, kan belum dibagikan kelasnya"
  k "Dibagikan?"

  "Huh? Kenapa dia bingung?"
  "Jangan-jangan di sekolah dulunya tidak ada pembagian kelas?!"

  a "Jadi di sekolah kita, satu angkatan akan dibagi dari kelas 12-A sampai 12-F"
  a "Yang mana pembagian itu akan berdasarkan dari hasil rapor siswa dari kelas sebelumnya, yaitu kelas 11, begitu..."
  k "Ohhh, kayaknya aku bakal masuk kelas F..."
  a "Pasti"
  k "..."
  a "Karena siswa maupun siswi baru juga akan dimasukkan ke kelas F."
  a "Aku gak ngerti kenapa akan otomatis masuk kelas F tanpa pertimbangan dahulu..."
  k "Bagus dong!"
  a "Eh-- Menurutku metodenya kurang bagus sih, tapi masuk akal juga."
  a "Mungkin maksud dari metodenya itu untuk menghargai para pelajar yang sudah lama dan akan naik ke kelas yang lebih tinggi dengan hasil yang ia raih."
  a "Jadi para pelajar baru gak bisa asal masuk dan menggantikan pelajar lama yang sudah berusaha"
  k "Ohhh, bisa jadi, bisa jadi"
  k "Tapi gimana nasib pelajar baru yang sama-sama sudah berusaha dengan keras tapi karena suatu kejadian, dia harus pindah sekolah dan masuk ke kelas paling bawah?"
  a "Nahhh... itu--"
  k "Hm?"
  a "A--"

  "Sial, aku sendiri gak tahu harus ngomong apa saat berada dalam kondisi ini"

  a "Ahahaha... aku sendiri gak tahu..."
  k "Hah! Sudah kuduga!"
  a "..."

  "Mukanya kenapa sangat menyebalkan..."

  "Kayaknya memang niat dari awal buat ngejatuhin aku..."

  k "Hahaha! Aku gak tahu kenapa, aku suka lihat wajah linglung kamu"
  a "!"

  "Oh-ohohokh..."
  "Sial, aku jadi senyum-senyum gak jelas"

  a "Makasih..."
  k "Buat apa?"

  "SIAL! KENAPA AKU MALAH BERTERIMA KASIH KEPADANYA?!"

  a "Aku cuman bahagia... ada orang yang bisa tertawa karena aku..."
  k "!"

  "SIALANNN!!! KENAPA AKU MALAH TERSENYUM?!?!"
  "RASANYA AKU TERSIPU MALU SEPERTI BUNGA PUTRI MALU!"

  k "Sama-sama"

  "SIAL! DIA TERSENYUM BALIK KEPADAKU!"
  "INI SEMUA SALAHKU! AKU SEHARUSNYA TIDAK BERBINCANG DENGANNYA!"
  "JIKA SAJA AKU--"

  k "Mau bertukar kontak?"
  a "Eh..."
  k "Siapa tahu kalau kita mau ketemuan saat hari-hari biasa..."

  "K-kenapa pipi dia memerah?!"
  "Jangan-jangan aku telah memikat hatinya? Hehe... hehehehe... mana mungkin...."

  a "O-ok, ini"

  "Aku mengambil hpku di saku celanaku dan memperlihatkan nomor HP-ku padanya"
  "Karina mulai memasukan nomorku ke kontaknya"
  "Ahhh..." 
  "seorang perempuan cantik menambahkan nomorku ke kontaknya..."
  "Aku sangat bahagia," 
  "saking bahagianya aku ingin membantai para lolicon di dunia ini"

  k "Dingdingding"

  "Dingdingding"
  "Pesan masuk dari Karina"

  kc "Halooo"
  ac "Olahhh"

  k "Olah?"
  a "Aku cuman ngebalik kata Halo"
  k "Ohh"
  k "Selamat Tuan Arda! Selamat!"

  "Huh? Kenapa dia memberikan aku ucapan selamat"

  a "Maaf Nyonya Karina, apa yang telah saya menangkan jika saya berkenan untuk bertanya akan perihal ini?"

  "Aku membalasnya bertanya dengan nada anggun agar kami selaras pada perbincangan lelucon ini"

  k "Anda adalah orang pertama yang memiliki nomor saya. Selamat Tuan Arda! Selamat!"

  "Aku adalah orang pertama?"
  "Bagaimana dengan--"
  "Ah...lebih baik aku tidak memikirkannya..."
  "Aku akan menjawabnya tanpa memikirkan hal itu..."

  a "Ah, seperti itu. Terima kasih atas informasi yang anda berikan, Nyonya Karina"

  "Kami berdua tertawa karena obrolan konyol kami sendiri"
  "Padahal yang kami lakukan hanya mengubah nada bicara, tapi aku tidak tahu kenapa bisa selucu ini"
  "Ya, sebenarnya bisa melihat senyuman manisnya pun sudah cukup bagiku"
  "Kami melanjutkan percakapan kami sampai kamu tiba di tujuan, yaitu kota Ciruka"
  "Sesampainya kami di stasiun Ciruka, aku mengakhiri percakapan kami dengan"

  a "Ah, kita sudah sampai"
  k "Oh, betul!"

  "Aku mulai mengenakan tas ranselku dan memasukkan HP-ku kesaku"
  "Aku berdiri dan menunggu Karina mengemas barangnya agar kami bisa keluar bersama"

  k "Ayo!"

  "Kami keluar dari gerbong D dan menginjakan kaki kami di atas stasiun kota Ciruka"

  a "Kayaknya sampai di sini aja, dah Karina"
  k "Dadah..."

  "Tujuanku sekarang adalah rumah, aku berjalan menuju rumah dengan tas ransel yang cukup berat di punggungku"

  a "Sekarang jam berapa ya?"

  "Aku bertanya-tanya sambil mengambil HP dari saku"

  a "Jam 20:31"

  "Ternyata sudah malam, pasti Ayah, Ibu dan Harris sedang menungguku di rumah"
  "Aku tak sabar untuk memainkan PS3 bersama Harris sepanjang hari"

  a "!"

  "Tiba-tiba ada orang yang menoel bahuku dari belakang"
  "Aku langsung membalikkan badanku"
  "Ternyata seperti dugaanku..."

  k "Kayaknya kita melewati arah yang sama, hehehe"
  a "Ehh, bisa begitu"

  "Aku mulai berjalan berdampingan dengan Karina, aku tetap menuju pada tujuanku yaitu, rumah"
  "Aku berjalan bersama Karina hanya karena arah yang kami lewati sama untuk beberapa meter kedepan, mungkin"
  "Atau mungkin tujuan kami adalah rumah masa depan kami?"
  "Hihihihi..."

  k "Ehh? Arda? Kenapa kamu tiba-tiba ketawa?"

  "Sial, aku keceplosan tertawa sendiri saat memikirkan hal itu!"

  a "E-enggak kenapa-kenapa, barusan aku cuman mikirin cara ngejahilin adikku doang"
  k "Hohhh... kamu tipe kakak yang usil ya, hehehe"
  a "Y-ya, kayanya begitu"

  "Fyuhhh... setidaknya dia tidak mencurigaiku akan hal yang aneh"

  k "Sebenarnya ini adalah hal baru bagiku..."
  a "Huh?"

  "Dia sedang membicarakan apa?"

  k "Berjalan bersama teman, rasanya seperti mimpi..."
  a "..."

  "Karina..."
  "Aku tidak tahu harus berkata apa..."

  k "Belum lagi di langit ada bintang dan bulan yang menerangi jalan yang kita lewati..."
  a "..."

  "Karina..."

  k "Entah berapa lama momen ini akan berlangsung, "
  k "Aku sudah bahagia dengan apa yang kulakukan sama kamu... Arda..."

  "..."

  k "M-maaf, rasanya kurang pantas jika aku berkata seperti itu..."
  k "Harusnya aku lebih tahu diri, maaf"
  a "G-gak, gak apa-apa kok"
  a "Aku juga senang bisa jalan bareng sama teman baru."
  a "Sensasi baru yang jarang aku rasain, apalagi malam kayak gini, dingin"
  k "Kamu suka rasa dingin?"
  a "Iya, habisnya nyaman. Kalau panas aku mudah berkeringat, hehehe"

  "Aku membalasnya dengan sebuah senyuman"
  "Dan ya, hawa malam ini sangat dingin... aku menyukainya"

  k "Arda..."

  "Entah kenapa dia tiba-tiba berhenti berjalan"

  a "Hm?"

  "Aku menjawabnya dengan nada yang lembut"

  k "A--"
  k "Aku!--"

  "Eoookkk"
  "Eh?"

  k "!"
  a "Hohhh..."
  k "..."

  "Hohhh..."

  a "Rumahku sudah tidak jauh dari sini kok, disana ada makanan enak. Biar aku tanya ke--"
  k "J-jangan! Aku lagi gak mau makan! Ehhh... apa itu namanya? Aku lagi deit! Ya! Deit!"
  a "Deit?"
  a "Maksudnya diet?"
  k "Iya itu! Jadi aku gak usah makan!"
  a "Yaaa... maksudnya diet itu bukan berarti kamu gak makan, cuman ada beberapa makanan yang dihindari dari jenis diet yang kamu lakuin sekarang"
  k "O-ohh..."
  a "Kalau gak makan artinya puasa, tergantung dari jam berapa hingga jam sekian"
  k "Ohhh..."
  a "Jadi mau makan sama apa?"
  k "Apa aja"

  "Smoooooth"

  k "E-eh, enggak, aku barusan ngomong tanpa pikir!"
  a "Kekurangan makanan mengakibatkan kekurangan energi yang membuat kerja otak tidak maksimal."
  a "ARTINYA KAMU HARUS MAKAN DI RUMAHKU!"
  a "BIAR OTAKMU BERKERJA MAKSIMAL!"

  "Aku sendiri tidak tidak tahu omong kosong apa yang aku ucapkan"
  "Tapi aku merasa sangat pintar setelah mengucapkan hal itu, hehehe..."

  k "Mari kita lanjut jalan saja"
  a "Hehhh... ok"

  "Aku menuruti perintahnya"
  "Aku sendiri kasihan jika dia terlalu malu untuk menanggapi apa yang aku katakan walaupun hanya sebuah candaan"
  "Hembusan angin malam melewati selah-selah rambutku"
  "Hembusan yang kurasakan ini sangat nyaman, karena aku sangat menyukai udara dingin"
  "Mataku menoleh kearah Karina..."
  "Hembusan angin ini tidak hanya melewati selah-selah rambutku, " 
  "Tapi juga melewati rambutnya Karina"
  "Rambut kuning keemasannya yang berterbangan..."
  "Apa yang kulihat ini bagaikan 7 keajaiban dunia"
  "Kecantikannya melepaskan dingin dari hari malam yang kurasakan"
  "Bagaimana bisa keluarganya punya masalah?"
  "Apa mereka tidak tahu jika mereka punya seorang malaikat yang harus dijaga?"
  "Saat aku melihat kedepan, ternyata beberapa langkah lagi aku sampai ke rumahku"

  a "Itu, rumahku di situ"

  "Aku menunjukan jari telunjukku ke arah rumahku"

  k "Ohhh..."
  a "Karina, rumah kamu masih jauh?"
  k "Enggak kok, sebentar lagi juga sampai"
  a "Kalau begitu biar aku anterin kamu sampai depan rumah kamu"

  "Aku melakukan ini karena aku peduli terhadapnya"
  "Aku tidak bisa membiarkan seorang malaikat berjalan sendirian di malam hari"
  "Yaaa... walaupun aku pernah meninggalkan dia di stasiun, karena aku pikir dia kita tidak memiliki arah yang sama"

  k "Gak usah kok"
  a "Gak apa-apa, dekat ini kok"
  k "Maksud aku dekat itu lumayan jauh, cuman aku sudah terbiasa saja"
  a "Yakin?"
  k "Iya, makasih sudah nawarin buat nganterin aku"

  "Tawaranku dibayar dengan senyuman hangat dari dia"

  a "Kalau begitu, bagaimana dengan makan di rumahku?"
  k "Aku gak terlalu lapar kok"
  a "Hahhh... ya sudah..."

  "Setidaknya aku sudah menawari dia..."

  "Aku sudah berada di depan rumahku, aku mengucapkan perpisahanku kepada Karina"

  a "Dah Karina, hati-hati di jalan ya"
  k "Dadah..."

  "Ucap Karina sambil berjalan melewati rumahku"

  a "Jangan lupa makan sesampai di rumahmu!"
  k "Ok!"

  "Saut kami berdua dengan suara sedikit kencang karena jarak kami mulai menjauh"
  "Aku berjalan menuju pintu rumahku"
  "Sesampainya aku di depan pintu rumah, aku menggerakan ganggang pintu"
  "Ckck"

  a "Huh?"

  "Terkunci?"
  "Aku membuka HP-ku dan mencoba untuk menelpon ayahku"
  "Jika aku berteriak dari sini, mereka tidak akan bisa dengar karena jarak dari kamar dan pintu depan lumayan jauh"

  a "Pesan masuk?"

  "Lama tak membuka HP-ku, ternyata ada pesan masuk dari jam 20:13"
  "Pesan itu dari Ibuku"
  "Aku membuka pesan dari ibuku"

  i "Arda, Ibu dan Ayah akan pergi ke tempat komputer Pak Nadi untuk beli spare part komputer baru buat ayah."
  i "Pas Ayah sama Pak Nadi ngobrolin tentang graphic card baru, ayah jadi pengen upgrade katanya..."
  i "Hadehhh..."
  i "Bisanya ngabisin duit doang emang dia tuh."
  i "Ibu juga sekalian mau beli provider baru, Komnet akhir-akhir ini harganya naik walaupun Ibu sudah jadi pelanggan setia, jadi pengen ganti ke SL. "
  i "Kalau kamu sudah sampe, telepon Harris aja, dia Ibu suruh buat nunggu kamu sampai datang. "
  i "Jangan lupa anterin Harris ke kamarnya dan langsung tidur sehabis tiba di rumah, Ok!"

  a "Iya"

  "Buset dah, panjang amat"
  "Kalau begitu aku cukup telepon si Harris, kasihan juga dia harus menungguku sampai tiba di rumah"
  "Bzzz... Bzzz..."
  "Telepon masuk?"

  a "Huh?"

  "Nomor ini sangat asing, mungkin ibu sudah mengganti kartunya"
  "Aku menjawab telepon itu dengan tenang"

  a "Halo"
  u "Halo Arda?"
  a "Ya, ada apa?"

  "Aku kira Ibuku yang menelpon"

  u "Kak Arda, sudah ada di rumah belum?"
  a "Belum, emangnya ada apa?"
  u "Ya sudah, kamu masuk dulu. Pasti capek karena perjalanankan"
  a "Oh, iya iya"
  b "Ya sudah, bibi matiin ya teleponnya. Dah..."
  a "Iya bi, dah..."

  "Aku kira siapa, ternyata bibiku. Seharusnya aku simpan nomor mereka..."
  "Hahhh..." 
  "Bodoh amat." 
  "Aku sangat capek hari ini, seakan-akan jiwaku disedot oleh tukang sedot WC"

  "Tak lama aku menelepon Harris"

  "Tuuuttt... Tuuuttt... Tuuuttt..."
  "Tuuuttt... Tuuuttt... Tuuuttt..."
  "Tuuuttt... Tuuuttt... Tuuuttt..."
  "Maaf--"

  "Sepertinya dia sedang tidur, lebih tepatnya ketiduran"
  "Kenapa Ibu mengandalkan Harris untuk hal seperti ini?"
  "Hahhh... Apa yang harus kulakukan..."

  a "HARRRIIISSS!!!"

  "Ini ide yang bodoh..."

  t "OI! JANGAN TERIAK-TERIAK MALAM KAYAK GINI! GIGI GUE SAKIT NIH!"
  a "M-MAAF PAK!"

  "Ya... seharusnya aku tidak berteriak..."

  u "Arda"

  "Suara yang tidak asing"

  u "Mungkin Harrisnya sudah tidur, mending nginep di rumah saya dulu aja"

  "Aku membalikan badanku, dan benar saja. Itu suara Michael, Ayahnya Lara"

  m "Gimana Arda? Di rumah juga masih ada makanan, siapa tahu kamu lapar sehabis perjalanan"
  a "Boleh, kalau begitu saya nginep aja kali ya... hehehe... maaf menganggu..."


  "Untungnya aku memiliki tetangga yang sudah seperti keluarga sendiri"
  "Jika tidak, mungkin aku sudah mati kedinginan tidur di halaman depan..."
  "Tcktck"

  am "!"
  h "Cepetan masuk..."

  "Si Kampret baru membuka pintunya..."

  m "Harris, tumben belum tidur"
  h "Eh, Pak Michael. Iya, barusan Ibu suruh aku buat jaga rumah."
  h "Katanya Kak Arda mau pulang malam in-- Hoammm..."
  m "Hohhh... mereka pasti jalan-jalan lagi..."
  a "Iya..."
  m "Hahhh... kebiasaan emang. Masa muda mereka belum larut ternyata, hahaha! Saya jadi iri"
  m "Ya sudah kalau begitu, kalian istirahat sekarang ya. Jangan begadang, awas kalau sampai begadang"
  a "Ok"
  h "Hmmm..."
  m "Ya sudah, dahhh..."
  a "Dahhh..."
  h "Dahhh..."

  "Ayahnya Lara berjalan ke rumahnya, rumahnya berada tepat di sebelah rumahku"
  "Jadi jika ada apa-apa, aku cukup pergi ke rumah sebelahku"
  "Hidup memang cukup menenangkan jika ada seseorang yang selalu terbuka untukmu"
  "Aku memasuki rumahku dengan muka yang sedikit masam, karena Harris yang lama membuka pintu"

  h "Gendong"

  "Punya adik menyebalkan sekali!"
  "Mau bagaimana lagi, diakan memang lemah dari kecil..."

  a "Iya-iya..."

  "Aku membungkukkan badanku agar punggungku bisa dinaiki olehnya"
  "Harris loncat kecil untuk meraih punggungku"
  "Hop"
  "Dia telah berada di punggungku"
  "Yang artinya..."

  a "Sip! Mari kita meluncur!"

  "Aku mulai membawanya sambil berlari-la--"

  h "Jangan..."

  a "Oh, ok... maaf ya"
  h "Hm..."

  "Dia sepertinya sangat lelah hari ini, mungkin di lain hari saja aku melakukannya"
  "Aku membawa Harris ke kamarnya, kamarnya berada tepat di sebelah kamarku"
  "Aku mencoba membuka pintu kamar Harris, tapi pintunya terkunci"

  a "Harris, kuncinya ada di ma--"
  h "Ini..."

  "Cepat tanggap"

  a "Sip"

  "Aku memasukan dan memutar kuncinya, pintu itu aku buka dengan perlahan, karena aku tidak suka dengan decitan pintu kamarnya yang setiap kali di buka atau di tutup selalu menghasilkan suara yang membuat telingaku ngilu dan mengganggu Harris"
  "Creakkk..."
  "Seperti yang kubilang, untungnya decitan itu tidak terlalu bising"
  "Aku berjalan menuju kasurnya Harris, dan menaruhnya tepat di atas kasur"

  a "Sip"
  h "Malam kak, hoammm..."
  a "Eh, sudah minum obatnya belum?"
  h "Hm..."
  "Ya... aku anggap sudah saja ..."

  a "Ya sudah, mimpi indahhh..."
  h "Hm..."

  "Aku keluar dari kamar Harris dan menutup pintunya dengan super pelan agar tidak menghasilkan suara"

  "Bzzz..."

  a "!"

  "CREAKKK!!!"

  h "Kakkk..."
  a "M-maaf, ada telepon masuk"

  "Sialan, siapa yang membuatku kaget seperti ini!"
  "Aku mulai berjalan ke kamarku sambil menjawab telepon yang membuatku sedikit marah..."
  "Walaupun begitu, aku menjawabnya dengan nada yang lembut." 
  "Aku tidak ingin menyakiti perasaan orang lain hanya karena kejadian yang tidak bisa dihindarkan"

  a "Halo"
  u "Halo Arda, kamu sudah di kamar?"
  a "Bibi?"
  b "Iya Arda, ini Bibi"
  a "Oh, jadi ada apa Bi?"

  "Aku membuka pintu kamarku dan memasukinya"

  b "Kamu sudah ada di kamar?"
  a "Sudah"
  b "Sudah nganterin Harris ke kamar berarti ya"
  a "Iya"
  b "Arda, jadi begini..."
  b "Ibu dan Ayah kamu kecelakaan..."

  "Ucapan yang aku dengar barusan tidak salahkan? Aku baru saja duduk di atas kasurku..."

  a "H-huh?"
  b "B-bibi tahu, ini benar-benar mengejutkan... Bibi hanya ingin tahu kau agar tidak terlalu memikirkannya di esok hari..."
  b "Besok adalah hari pertama kalian masuk sekolah... jadi Bibi ingin kalian untuk tetap berada di rumah"

  "Apa maksud dari tidak terlalu memikirkannya di esok hari?"
  "Yang dia lakukan hanyalah membuatku tidak bisa tidur sepanjang malam dengan kabar yang ia berikan..."
  "Kecelakaan..."
  "Kapan? Di mana? Bagaimana?"
  "Bagaimana?"
  "Setidaknya mereka masih bernafaskan?"

  b "..."
  b "Bibi sendiri tidak tahu... huuu--uuu"

  "Hah... hahaha... pikiranku terucap kembali..."

  a "Hiks... I-ibu... Ayah... mereka... hiks... mereka akan baik-baik saja kan?"
  b "..."

  "Jawablah Bi..."
  "Jawab..."
  "JAWABBB!!!"

  b "Akupun tidak tahu! Hiks..."
  b "Yang aku tahu mereka sedang dalam kondisi yang sangat kritis..."

  "Sial..."
  "Sialan..."
  "Kenapa mereka..."
  "Kenapa tidak aku saja..."
  "Aku harus beritahu Harris--"

  b "JANGAN!"
  b "Jangan... biar Bibi yang akan memberitahunya besok"
  a "Bibi akan meneleponnya?"
  b "Tidak, Bibi akan kesana"

  "Dia ada benarnya, tidak bagus juga jika aku memberitahunya." 
  "Harris membutuhkan istirahat yang cukup setelah menunggu semalaman"
  "Aku masih ingin tahu apa yang terjadi dengan orang tuaku secara rinci..."

  a "Bi..."
  b "Ya?"

  "Aku menaruh tanganku di dada..."
  "Aku menekan tanganku pada dadaku dengan kuat..."
  "Aku harus menanyakannya..."
  "Aku harus..."

  a "ERGHHH!!!"

  "Aku terjatuh kebawah dari atas kasurku"
  "Apa ini?!"
  "Sakit di dada ini?!"

  b "Arda?! ARDA?!"

  "Sialan..."

  a "Harghhh... harghhh... naf--harghhh..."
  b "ARDA?! ARDAAA?! KAMU KENAPA?!"

  "SIAL!"

  a "Harghhh..... harghhh..... harghhh....."
  b "Bibi panggilkan ambulan ke rumahmu secepatnya!"
  a "J-jangan--harghhh... tungg--harghhh..."

  "Bajingan..."
  "Apa aku terkena serangan jantung?!"

  a "Kughhh!"
  b "Apa kau yakin?!"

  menu:
    "Yakin":
      jump good_scene3
    "Tidak Yakin":
      jump good_scene3
    "Tidak Tahu":
      jump good_scene3

  return


label good_scene3:
  a "Ya... harghhh..."

  "Tahan Arda... Tahan..."
  "Tahan..."
  "Taaa--hannnn..."
  "Tarik nafas..."

  a "Hufffff....."
  a "Hahhhhh....."
  a "Hufffff....."
  a "Hahhhhh....."
  a "Hahhh... hahhh... hahhh..."

  "..."
  "....."
  ".........."

  b "ARDA?! KAMU BAIK-BAIK SAJA?!"
  a "I-iya Bi, sepertinya aku baru saja terkena serangan panik"

  "Aku berdiri secara pelahan mengangkat tubuhku dengan menggunakan kasurku sebagai penopang"
  "Aku duduk di atas kasurku dengan pelahan"
  "Aku terlalu berlebihan dengan mengganggap bahwa aku terkena serangan jantung"
  "Ternyata yang aku alami hanyalah serangan panik, hahaha... ha... ha... ha...?"

  b "Apa perlu Bibi panggilkan ambulan sekarang? Bibi tidak ingin ada hal buruk yang terjadi padamu"
  a "Tidak. Aku baik-baik saja sekarang, aku tidak perlu itu..."
  a "Yang aku butuhkan sekarang adalah istirahat..."
  b "Apa kamu yakin?"
  a "Iya Bi, terima kasih atas perhatiannya"
  b "Y-ya, sama-sama"
  a "Kalau begitu sekarang aku ingin tidur, Bi. Selamat malam"
  b "Ya, istirahatkan dirimu. Selamat malam"

  "Aku mematikan HP-ku dan menaruhnya di samping bantalku"
  "Aku berbaring di atas kasurku, kepalaku penuh dengan pikiran buruk"

  a "Apa yang harus kulakukan..."

  "Kenapa ini bisa terjadi..."
  "Apakah aku dan Harris akan tinggal sendirian...?"
  "Apakah salah satu orang dari keluarga Ayah dan Ibu akan mengadopsi kami?"
  "Bagaimana jika tidak...?"
  "Apakah aku harus mulai mencari pekerjaan?"
  "Bagaimana jika aku meninggalkan Harris dan dia mengalami hal yang buruk di saat aku tidak ada di rumah?"
  "Bagaimana caranya agar aku bisa membelikan dia makanan, minuman dan obat yang dia perlukan...?"


  a "Kenapa..."
  a "KENAPAAA--! Aghhhaghhhaghhh..."
  a "Kenapa?!"
  a "Kenapa..."
  a "Kenapa ini bisa terjadi pada kami..."

  "Jeritan tangisku aku sembunyikan dalam bantalku..."
  "Hanya kamarku yang bisa melihat betapa menyedihkannya aku sekarang"
  "Orang yang menangis ini tidak memiliki tempat awal untuk memulai"
  "Dia sudah berada di tengah-tengah"
  "Dia tidak tahu harus mulai darimana"
  "Dia hanya bisa menangis"
  "Mengeluarkan semua kesedihannya"
  "Dia adalah aku..."
  "Arda"
  "Orang yang sangat tidak berguna..."
  "Orang yang tidak memiliki arah..."
  "Orang yang mencoba untuk merasakan awal hidup yang baru..."
  "Dimulai dari hari esok..."
  "Dia akan merasakan pahitnya dunia."

  return

label bad_end:
  "BAD END"

  return

label good_end:
  "GOOD END"

  return  
