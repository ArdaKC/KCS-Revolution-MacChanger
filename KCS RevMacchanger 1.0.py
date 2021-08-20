from datetime import datetime
from random import choice
import os


PATH2 = "./dil.txt"
language1 = ""
language2 = ""
if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
    with open("dil.txt", "r") as f:
        language2 = f.read()
        language1 = language2
else:
   print("dilinizi seçin. \ select your language.")
   print("Turkish : 1")
   print("English : 2")
   language1 = input("")
   with open("dil.txt", "w") as f:
       f.write(language1)
language = ""
language = language1

if language == "1":

    PATH = './ayar1.txt'
    PATH2 = "./arayüz.txt"
    ayarlar = ""
    if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
        with open("arayüz.txt", "r") as f:
            arayüzconfig = f.read()

    else:
      arayüzconfig = "00"
    arayüzconfig1 = arayüzconfig
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):

        with open("ayar1.txt", "r") as f:
            ayarlar = f.read()

    else:
        ayarlar = "00"
    ayarlar1 = ayarlar
    print("KCS RevolutionMacChanger 1.0")
    print("MAC Değiştirmek için            : 1")
    print("Gerekli Paketleri Yüklemek için : 2")
    print("Hakkında Kısmına Bakmak İçin    : 3")
    print("Ayarlamalar Yapmak için         : 4")
    print("Random MAC Oluşturmak İçin      : 5")
    print("MAC Geçmişini Göster            : 6")
    print("Çıkış yap                       : X")

    secenek = input("")
    if secenek == "6":
        PATH2 = './macgecmisi.txt'
        if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
               os.system("nano macgecmisi.txt")
        else:
            print("mac gecmisi dosyası bulunamadı.")

    if secenek == "X" or "x":
        os.system("exit")
    if secenek == "5":
        print("kaç tane mac oluşturulsun?")
        macsayısı1 = input()
        macsayısı = int(macsayısı1)

        karakterler = "01234567890123456789abcedfg"
        sadecesayı = "1234567890"
        sadeceharf = "abceYAdfg"
        sadecekucuksayılar = "012345"
        sadecebuyuksayılar = "6789"
        for i in range(macsayısı):
            mac1 = ""
            mac2 = ""
            mac3 = ""
            mac4 = ""
            mac5 = ""
            mac6 = ""
            mac1_1 = ""
            mac2_2 = ""
            mac3_3 = ""
            mac4_4 = ""
            mac5_5 = ""
            mac6_6 = ""
            mac1 += str(choice(karakterler))
            mac2 += str(choice(karakterler))
            mac3 += str(choice(karakterler))
            mac4 += str(choice(karakterler))
            mac5 += str(choice(karakterler))
            mac6 += str(choice(karakterler))
            mac1_1 += str(choice(karakterler))
            mac2_2 += str(choice(karakterler))
            mac3_3 += str(choice(karakterler))
            mac4_4 += str(choice(karakterler))
            mac5_5 += str(choice(karakterler))
            mac6_6 += str(choice(karakterler))
            mac = mac1 + mac1_1 + ":" + mac2 + mac2 + ":" + mac3 + mac3_3 + ":" + mac4 + mac4_4 + ":" + mac5 + mac5 + ":" + mac6 + mac6_6
            print("mac : " + mac)
    if secenek == "3":
        print("Bu Uygulama Arda KC Tarafından Yapılmıştır.")
    if secenek == "2":
        print("Hangi dağıtımı kullanıyorsunuz?")
        print("ARCH : 1")
        print("OPENSUSE : 2")
        print("Debian & Ubuntu : 3")
        print("Fedora : 4")
        dagitim = input("")

        if dagitim == "1":
            os.system("pacman -Syy")
            os.system("pacman -S net-tools-deprecated")
            os.system("pacman -S nano")
            print("İşlem tamamlandi!")

        if dagitim == "2":
            os.system("zypper refresh")
            os.system("zypper install net-tools-deprecated")
            os.system("zypper install nano")
            print("İşlem tamamlandi!")

        if dagitim == "3":
            os.system("apt update")
            os.system("apt install net-tools -y")
            os.system("apt install nano")
            print("İşlem tamamlandi!")
        if dagitim == "4":
            os.system("dnf upgrade --refresh")
            os.system("dnf install net-tools")
            os.system("dnf install net-tools-deprecated")
            os.system("dnf install nano")
            print("İşlem tamamlandi!")

    if secenek == "4":
        print("Otomatik MAC Oluşturmayı kapatmak için             : 1")
        print("Mac Gecmisini Etkinleştir                          : 2")
        print("Sürekli Aynı Arayüzü Yazmamak Üzere Arayüzü Kaydet : 3")
        print("Dil Ayarları.                                      : D")
        print("Ayarları Sıfırla                                   : R")
        ayar = input("")


        if ayar == "D":

            language1 = ""
            language2 = ""

            print("dilinizi seçin. \ select your language.")
            print("Turkish : 1")
            print("English : 2")
            language1 = input("")
            with open("dil.txt", "w") as f:
                f.write(language1)
                print("Dil Başarıyla Ayarlandı Tekrar Açtığınız'Da Seçtiğiniz Dil Gösterilecek.")

        if ayar == "3":
            os.system("ifconfig")
            print("Kullanılacak arayüzü yazın.")
            arayüz = input("")
            with open("arayüz.txt", "w") as f:
              f.write(arayüz)
              print("arayüz başarıyla kayıt edildi.")

        if ayar == "R":
            PATH = './ayar1.txt'
            PATH3 = "./arayüz.txt"
            PATH4 = "./dil.txt"
            if os.path.isfile(PATH3) and os.access(PATH3, os.R_OK):
                 print("arayüz yapılandırması sıfırlansın mı? evet/hayır")

                 soru = input("")
                 if soru == "evet":

                     os.remove("arayüz.txt")
                     print("arayüz.txt başarıyla silindi.")
                 else:
                     print("arayüz.txt dosyası es gecildi.")
            if os.path.isfile(PATH4) and os.access(PATH4, os.R_OK):
                print("dil ayarları sıfırlansın mı? Evet/Hayır")

                soru = input("")
                if soru == "evet":

                    os.remove("dil.txt")
                    print("dil.txt başarıyla silindi.")
                else:
                    print("dil.txt dosyası es gecildi.")
            if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                os.remove("ayar1.txt")

                print("ayarlar başarıyla sıfırlandı.")

            else:
                print("ayar1.txt dosyası bulunamadı zaten bir ayar yapılmamış.")
        if ayar == "2":
           with open("ayar1.txt", "a") as f:
               f.write(ayar)
               print("ayar başarıyla uygulandı")
        if ayar == "1":
           with open("ayar1.txt", "a") as f:
               f.write(ayar)
               print("ayar başarıyla uygulandı.")
    if secenek == "1":


     os.system("ifconfig")
     if arayüzconfig1 == "00":
         print("MAC Adresinin Değiştirilmesini istediğin arayüzü yaz.")

         arayüz = input("arayüz:")

     else:
         arayüz1 = ""
         arayüz1 = arayüzconfig

     arayüz = arayüz1
     a = 20
     PATH2 = './ayar1.txt'
     if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
         with open("ayar1.txt", "r") as f:
             ayarlar2 = f.read()
     else:
         print("")
         ayarlar2 = ""
     ayarlar3 = ayarlar2
     if ayarlar1.find("1") == -1:

      while a > 10:

          karakterler = "01234567890123456789abcedfg"
          sadecesayı = "1234567890"
          sadeceharf = "abceYAdfg"
          sadecekucuksayılar = "012345"
          sadecebuyuksayılar = "6789"
          for i in range(100):
             mac1 = ""
             mac2 = ""
             mac3 = ""
             mac4 = ""
             mac5 = ""
             mac6 = ""
             mac1_1 = ""
             mac2_2 = ""
             mac3_3 = ""
             mac4_4 = ""
             mac5_5 = ""
             mac6_6 = ""
             mac1 += str(choice(karakterler))
             mac2 += str(choice(karakterler))
             mac3 += str(choice(karakterler))
             mac4 += str(choice(karakterler))
             mac5 += str(choice(karakterler))
             mac6 += str(choice(karakterler))
             mac1_1 += str(choice(karakterler))
             mac2_2 += str(choice(karakterler))
             mac3_3 += str(choice(karakterler))
             mac4_4 += str(choice(karakterler))
             mac5_5 += str(choice(karakterler))
             mac6_6 += str(choice(karakterler))
             mac = mac1 + mac1_1 + ":" + mac2 + mac2 + ":" + mac3 + mac3_3 + ":" + mac4 + mac4_4 + ":" + mac5 + mac5 + ":" + mac6 + mac6_6
             if mac2 == mac5:
                 for i in range(100):
                      eşitlikboz = ""
                      eşitlikboz += str(choice(karakterler))
                      mac5 = eşitlikboz
          pass
          if os.system("ifconfig " + arayüz + " down") == 0:
             print("arayüz düşürme başarılı oldu.")

             if os.system("ifconfig " + arayüz + " hw " + "ether " + mac) == 0:
                 print("mac değiştirme işlemi başarılı")
                 print("yeni mac adresi : " + mac)
                 if ayarlar3.find("2") ==-1:
                     print("")
                 else:
                     with open("macgecmisi.txt", "a") as f:

                         now = datetime.now()
                         day = now.strftime("%Y:%m:%d")
                         time = now.strftime("%H:%M:%S")

                         f.write("\n" + day + " : " + time + " : " + mac)
                         print("MAC Adresi macgecmisi.txt dosyasına kayıt edildi.")

                 a = 1
                 if os.system("ifconfig " + arayüz + " up") == 0:
                   print("işlemler tamamlandı.")
             else:
               print("mac değiştirme işlemi başarısız oldu.")
               print("yeni mac adresi oluşturularak tekrar deneniyor...")
          else:
            print("arayüz düşürme başarısız oldu.")
            a = 1
     else:
         print("MAC Adresi Belirtin örnek 22:33:44:55:66:77")
         custom_mac = input("adress: ")
         if os.system("ifconfig " + arayüz + " down") == 0:
             print("arayüz düşürme başarılı oldu.")

             if os.system("ifconfig " + arayüz + " hw " + "ether " + custom_mac) == 0:
                 print("mac değiştirme işlemi başarılı")
                 print("yeni mac adresi : " + custom_mac)

                 if os.system("ifconfig " + arayüz + " up") == 0:
                     print("işlemler tamamlandı.")
             else:
                 print("mac değiştirme işlemi başarısız oldu.")
                 print("yeni mac adresi oluşturularak tekrar deneniyor...")
         else:
             print("arayüz düşürme başarısız oldu.")

else:
    PATH = './ayar1.txt'
    PATH2 = "./arayüz.txt"
    ayarlar = ""
    if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
        with open("arayüz.txt", "r") as f:
            arayüzconfig = f.read()

    else:
        arayüzconfig = "00"
    arayüzconfig1 = arayüzconfig
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):

        with open("ayar1.txt", "r") as f:
            ayarlar = f.read()

    else:
        ayarlar = "00"
    ayarlar1 = ayarlar
    print("KCS RevolutionMacChanger 1.0")
    print("Change MAC                      : 1")
    print("İnstall required packages       : 2")
    print("Look Who Created This Software  : 3")
    print("Open Settings                   : 4")
    print("Create Random MAC               : 5")
    print("Show MAC History                : 6")
    print("Exit                            : X")

    secenek = input("")
    if secenek == "6":
        PATH2 = './macgecmisi.txt'
        if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
               os.system("nano macgecmisi.txt")
        else:
            print("MAC history file not found.")

    if secenek == "X" or "x":
        os.system("exit")
    if secenek == "5":
        print("how many Macs to create?")
        macsayısı1 = input()
        macsayısı = int(macsayısı1)

        karakterler = "01234567890123456789abcedfg"
        sadecesayı = "1234567890"
        sadeceharf = "abceYAdfg"
        sadecekucuksayılar = "012345"
        sadecebuyuksayılar = "6789"
        for i in range(macsayısı):
            mac1 = ""
            mac2 = ""
            mac3 = ""
            mac4 = ""
            mac5 = ""
            mac6 = ""
            mac1_1 = ""
            mac2_2 = ""
            mac3_3 = ""
            mac4_4 = ""
            mac5_5 = ""
            mac6_6 = ""
            mac1 += str(choice(karakterler))
            mac2 += str(choice(karakterler))
            mac3 += str(choice(karakterler))
            mac4 += str(choice(karakterler))
            mac5 += str(choice(karakterler))
            mac6 += str(choice(karakterler))
            mac1_1 += str(choice(karakterler))
            mac2_2 += str(choice(karakterler))
            mac3_3 += str(choice(karakterler))
            mac4_4 += str(choice(karakterler))
            mac5_5 += str(choice(karakterler))
            mac6_6 += str(choice(karakterler))
            mac = mac1 + mac1_1 + ":" + mac2 + mac2 + ":" + mac3 + mac3_3 + ":" + mac4 + mac4_4 + ":" + mac5 + mac5 + ":" + mac6 + mac6_6
            print("mac : " + mac)
    if secenek == "3":
        print("This software created by arda kc.")
    if secenek == "2":
        print("Which Linux Distro You're Using?")
        print("ARCH : 1")
        print("OPENSUSE : 2")
        print("Debian & Ubuntu : 3")
        print("Fedora : 4")
        dagitim = input("")

        if dagitim == "1":
            os.system("pacman -Syy")
            os.system("pacman -S net-tools-deprecated")
            os.system("pacman -S nano")
            print("Operation completed.")

        if dagitim == "2":
            os.system("zypper refresh")
            os.system("zypper install net-tools-deprecated")
            os.system("zypper install nano")
            print("Operation completed.")

        if dagitim == "3":
            os.system("apt update")
            os.system("apt install net-tools -y")
            os.system("apt install nano")
            print("Operation completed.")
        if dagitim == "4":
            os.system("dnf upgrade --refresh")
            os.system("dnf install net-tools")
            os.system("dnf install net-tools-deprecated")
            os.system("dnf install nano")
            print("Operation completed.")

    if secenek == "4":
        print("Disable Automatic Mac Creation                                  : 1")
        print("Enable MAC History                                              : 2")
        print("Save Interface So As Not To Write The Same Interface Constantly : 3")
        print("Language Settings                                               : D")
        print("Reset Settings                                                  : R")
        ayar = input("")

        if ayar == "D":
            language1 = ""
            language2 = ""

            print("dilinizi seçin. \ select your language.")
            print("Turkish : 1")
            print("English : 2")
            language1 = input("")
            with open("dil.txt", "w") as f:
                f.write(language1)
                print("Language Set Successfully When You Open It Again, The Language You Selected Will Be Shown.")

        if ayar == "3":
            os.system("ifconfig")
            print("Type the interface to save.")
            arayüz = input("")
            with open("arayüz.txt", "w") as f:
                f.write(arayüz)
                print("interface successfully saved.")

        if ayar == "R":
            PATH = './ayar1.txt'
            PATH3 = "./arayüz.txt"
            PATH4 = "./dil.txt"
            if os.path.isfile(PATH3) and os.access(PATH3, os.R_OK):
                print("reset interface configuration? yes/no")

                soru = input("")
                if soru == "yes":

                    os.remove("arayüz.txt")
                    print("arayüz.txt deleted sucessfully.")
                else:
                    print("arayüz.txt named File not deleted.")
            if os.path.isfile(PATH4) and os.access(PATH4, os.R_OK):
                print("Do you want to reset language settings? yes/no")

                soru = input("")
                if soru == "yes":

                    os.remove("dil.txt")
                    print("arayüz.txt deleted sucessfully.")
                else:
                    print("arayüz.txt named File not deleted.")
            if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                os.remove("ayar1.txt")

                print("settings successfully reseted to default")

            else:
                print("ayar1.txt File Not Found already a setting has not been made.")
        if ayar == "2":
            with open("ayar1.txt", "a") as f:
                f.write(ayar)
                print("setting applied successfully.")
        if ayar == "1":
            with open("ayar1.txt", "a") as f:
                f.write(ayar)
                print("setting applied successfully.")
    if secenek == "1":

        os.system("ifconfig")
        if arayüzconfig1 == "00":
            print("Write down the interface where you want the MAC address changed.")

            arayüz = input("arayüz:")

        else:
            arayüz1 = ""
            arayüz1 = arayüzconfig

        arayüz = arayüz1
        a = 20
        PATH2 = './ayar1.txt'
        if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
            with open("ayar1.txt", "r") as f:
                ayarlar2 = f.read()
        else:
            print("")
            ayarlar2 = ""
        ayarlar3 = ayarlar2
        if ayarlar1.find("1") == -1:

            while a > 10:

                karakterler = "01234567890123456789abcedfg"
                sadecesayı = "1234567890"
                sadeceharf = "abceYAdfg"
                sadecekucuksayılar = "012345"
                sadecebuyuksayılar = "6789"
                for i in range(100):
                    mac1 = ""
                    mac2 = ""
                    mac3 = ""
                    mac4 = ""
                    mac5 = ""
                    mac6 = ""
                    mac1_1 = ""
                    mac2_2 = ""
                    mac3_3 = ""
                    mac4_4 = ""
                    mac5_5 = ""
                    mac6_6 = ""
                    mac1 += str(choice(karakterler))
                    mac2 += str(choice(karakterler))
                    mac3 += str(choice(karakterler))
                    mac4 += str(choice(karakterler))
                    mac5 += str(choice(karakterler))
                    mac6 += str(choice(karakterler))
                    mac1_1 += str(choice(karakterler))
                    mac2_2 += str(choice(karakterler))
                    mac3_3 += str(choice(karakterler))
                    mac4_4 += str(choice(karakterler))
                    mac5_5 += str(choice(karakterler))
                    mac6_6 += str(choice(karakterler))
                    mac = mac1 + mac1_1 + ":" + mac2 + mac2 + ":" + mac3 + mac3_3 + ":" + mac4 + mac4_4 + ":" + mac5 + mac5 + ":" + mac6 + mac6_6
                    if mac2 == mac5:
                        for i in range(100):
                            eşitlikboz = ""
                            eşitlikboz += str(choice(karakterler))
                            mac5 = eşitlikboz
                pass
                if os.system("ifconfig " + arayüz + " down") == 0:
                    print("interface down was successful.")

                    if os.system("ifconfig " + arayüz + " hw " + "ether " + mac) == 0:
                        print("Mac replacement successful.")
                        print("new mac address : " + mac)
                        if ayarlar3.find("2") == -1:
                            print("")
                        else:
                            with open("macgecmisi.txt", "a") as f:

                                now = datetime.now()
                                day = now.strftime("%Y:%m:%d")
                                time = now.strftime("%H:%M:%S")

                                f.write("\n" + day + " : " + time + " : " + mac)
                                print("MAC address saved to txt file.")

                        a = 1
                        if os.system("ifconfig " + arayüz + " up") == 0:
                            print("operations complete.")
                    else:
                        print("Mac replacement failed.")
                        print("creating a new mac address and trying again...")
                else:
                    print("interface down failed.")
                    a = 1
        else:
            print("Specify MAC address example 22:33:44:55:66:77")
            custom_mac = input("adress: ")
            if os.system("ifconfig " + arayüz + " down") == 0:
                print("interface down was successful.")

                if os.system("ifconfig " + arayüz + " hw " + "ether " + custom_mac) == 0:
                    print("Mac replacement successful.")
                    print("new mac address : " + custom_mac)
                    if ayarlar3.find("2") == -1:
                        print("")
                    else:
                        with open("macgecmisi.txt", "a") as f:

                            now = datetime.now()
                            day = now.strftime("%Y:%m:%d")
                            time = now.strftime("%H:%M:%S")

                            f.write("\n" + day + " : " + time + " : " + mac)
                            print("MAC address saved to txt file.")

                    if os.system("ifconfig " + arayüz + " up") == 0:
                        print("operations completed.")
                else:
                    print("Mac replacement failed.")
                    print("creating a new mac address and trying again...")
            else:
                print("interface downgrade failed.")
