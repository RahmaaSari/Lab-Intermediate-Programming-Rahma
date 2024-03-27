#fungsi untuk menampilkan tebakan benar
def Yangditebak(word,huruf_tebakan):
    ditebak = ''
    for i in word:
        if i in huruf_tebakan:
            ditebak+= (i)
        else:
            ditebak+='_'
    return ditebak
#fungsi untuk bermain
def hangman(word):
  chance = 6 
  huruf_tebakan = []
  while chance > 0 :
    print("Masukkan sebuah huruf tebakan")
    tebakan = input('Huruf:')
    if not tebakan.isalpha():
      tebakan = input('Masukan huruf:')
    elif len(tebakan) != 1:
      tebakan = input('Masukan sebuah huruf:')
    elif tebakan in huruf_tebakan:
      tebakan = input('Kamu telah menebak huruf tersebut, silahkan masukkan huruf lain:')
    else:
      huruf_tebakan += tebakan
      if tebakan not in word:
          chance -= 1
          print('Tebakan salah')
          print('Kesempatan tersisa:', chance)
      else:
          print('Tebakan benar')
          print('Kesempatan tersisa:', chance)
          print('Tebakan:',Yangditebak(word, huruf_tebakan))
          if '_' not in Yangditebak(word, huruf_tebakan):
            print('Selamat kamu berhasil menebak kata rahasia:',word)
            break
  if chance == 0:
    print('Kamu kalah')
    print('Kamu kehabisan kesempatan menebak')
    print('Kamu kalah!')
    print('Kata yang benar adalah:', word)

#Baris yang memanggil fungsi hangman(kata_rahasia)
hangman('kucing')