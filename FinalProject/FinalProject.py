questions = ["En çok bilinen şarkılarından bazıları “Yesterday”, “Hey Jude”, “Michelle” olan ve ayrıca Liverpool şehriyle anılan bir zamanların dünyaca ünlü İngiliz pop grubu hangisidir?"," Sanayi devrimi ilk olarak hangi ülkede gerçekleşmiştir?",
" Atatürk’ün de heykeli bulunan ünlü mumya müzesi Madame Tussauds hangi şehirdedir?", "Bir dönem İskandinav ülkelerinde hüküm sürmüş, yılın büyük kısmını denizlerde geçiren savaşçı halk aşağıdakilerden hangisidir?", 
"Ünlü İspanyol ressam ve heykeltraş Pablo Picasso hangi akımın öncüsüdür?", "Sessiz filmleriyle tanınan ve Şarlo karakteri ile özdeşleşen dünya çapında üne sahip İngiliz komedi aktörü kimdir?",
"Hangi Alman besteci hayatının ikinci yarısını sağır olarak geçirmiştir ve buna rağmen Fidelio operasına imza atmıştır?", "“İki Şehrin Hikayesi” ve “Büyük Umutlar” gibi 19. yüzyıla ait romanların sahibi ünlü İngiliz yazar kimdir?",
" “Adriyatik’in Kraliçesi’ olarak bilinen ve ünlü San Marco Meydanı ile tanınan hangi İtalyan şehri su üzerinde kurulmuştur?", "Atatürk; “Bugün vatanımızda bir milli kudret varsa, o cereyan, felaketlerden ders alan ulusun kalp ve dimağından doğmuştur” diyerek aşağıdakilerden hangisinin önemine vurgu yapmıştır"]

answer1 = ["A) Pink Floyd", "B) The Beatles", "C) Abba", "D) Queen"] #b
answer2 = ["A) Almanya ", "B) İtalya", "C) İngiltere", "D) Fransa"]  #c
answer3 = ["A) Paris ", "B) Berlin", "C) Londra", "D) Rotterdam"]  #c
answer4 = ["A) Keltler ", "B) Aztekler", "C) Anglo-saksonlar", "D) Vikingler"]  #d
answer5 = ["A) İmpresyonizm ", "B) Kübizm", "C) Sürrealizm", "D) Fütürizm"]  #b
answer6 = ["A) Tony Blair ", "B) Elvis Presley", "C) Charlie Chaplin", "D) Alfred Hitchcock"]  #c
answer7 = ["A) L. van Beethoven ", "B) J. S. Bach", "C) R. Wagner", "D) F.Schubert"]  #a
answer8 = ["A) C.Dickens", "B) T. Jansson", "C) B. Brecht", "D) F. Kafka"]  #a
answer9 = ["A) Roma", "B) Venedik", "C) Cenova", "D) Brindisi"]  #b
answer10 = ["A) Milli egemenlik", "B) Milli birlik ve beraberlik", "C) Barışçılık", "D) Evrensellik"]  #b

answers =["B","C", "C", "D", "B", "C", "A", "A", "B","B"]


def knowledge():
   
   puan = 100
   
   print("Soru 1: ", questions[0])
   for x in answer1:
      print(x)
   useranswer1 = input("Cevap Şıkkınız: ") 
   if useranswer1.upper() == answers[0]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10

   print("Soru 2: ", questions[1])
   for x in answer2:
      print(x)
   useranswer2 = input("Cevap Şıkkınız: ") 
   if useranswer2.upper() == answers[1]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10      

   print("Soru 3: ", questions[2])
   for x in answer3:
      print(x)
   useranswer3 = input("Cevap Şıkkınız: ")
   if useranswer3.upper() == answers[2]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10   

   print("Soru 4: ", questions[3])
   for x in answer4:
      print(x)
   useranswer4 = input("Cevap Şıkkınız: ") 
   if useranswer4.upper() == answers[3]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10

   print("Soru 5: ", questions[4])
   for x in answer5:
      print(x)
   useranswer5 = input("Cevap Şıkkınız: ") 
   if useranswer5.upper() == answers[4]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10      

   print("Soru 6: ", questions[5])
   for x in answer6:
      print(x)
   useranswer6 = input("Cevap Şıkkınız: ") 
   if useranswer6.upper() == answers[5]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10   

   print("Soru 7: ", questions[6])
   for x in answer7:
      print(x)
   useranswer7 = input("Cevap Şıkkınız: ") 
   if useranswer7.upper() == answers[6]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10   

   print("Soru 8: ", questions[7])
   for x in answer8:
      print(x)
   useranswer8 = input("Cevap Şıkkınız: ") 
   if useranswer8.upper() == answers[7]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10 

   print("Soru 9: ", questions[8])
   for x in answer9:
      print(x)
   useranswer9 = input("Cevap Şıkkınız: ") 
   if useranswer9.upper() == answers[8]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10     

   print("Soru 10: ", questions[9])
   for x in answer10:
      print(x)
   useranswer10 = input("Cevap Şıkkınız: ") 
   if useranswer10.upper() == answers[9]: #According To Case Sensitivity
      print("Tebrikler Cevabınız Doğru")
      puan = puan
   else:
      print("Cevabınız Yanlış")
      puan -= 10   

   if puan >= 60:
      print(f"Tebrikler Yarışma Sonucunuz Başarılı Puanınız: {puan}")  
   else:
      print(f"Üzgünüz Yarışma Sonucunuz Başarısız Puanınız: {puan}")   

print("Merhabalar! Bilgi Yarışmamıza Hoşgeldiniz! Umarım Eğlenceli Vakit Geçirirsiniz! Başarılar!")
knowledge()
print("Bilgi Yarışması Bitmiştir! Katıldığınız için Teşekkürler!")

       
   