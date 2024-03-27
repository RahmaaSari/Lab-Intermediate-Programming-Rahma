import random
#fungsi untuk menampilkan tebakan benar
def Yangditebak(word,huruf_tebakan):
    ditebak = ''
    for i in word:
        if i in huruf_tebakan:
            ditebak+= (i+' ')
        else:
            ditebak+='_ '
    return ditebak
#fungsi untuk bermain
def hangman(word):
  global win_score
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
            score+=1
            print('skor kemenangan:',win_score)
            break
  if chance == 0:
    print('Kamu kalah')
    print('Kamu kehabisan kesempatan menebak')
    print('Kamu kalah!')
    print('Kata yang benar adalah:', word)
    print('skor kemenangan:',win_score)

#fungsi untuk memilih kata rahasia
def pilih_kata():
  kata_rahasia = rahasia[random.randint(0,len(rahasia)-1)]
  #kata_rahasia = random.choice(rahasia)
  rahasia.remove(kata_rahasia)
  return kata_rahasia


#fungsi untuk memulai permainan
def main():
  if len(rahasia) > 0:
    hangman(pilih_kata())
    main_lagi()
  else:
    print('Kamu telah menebak semua kata rahasia')
    return print('skor kemenangan:',win_score)

#fungsi untuk mengulang permainan
def main_lagi():
  global win_score
  while True:
    main_lagi = input('Mau main lagi? (Y/N):')
    if main_lagi.upper() == 'Y':
      main()
    elif not main_lagi.isalpha() or len(main_lagi) != 1:
      continue
    else:
      print('skor kemenangan:',win_score)
      break

rahasia = ['dunia','universal','superhero']
win_score = 0
main()
