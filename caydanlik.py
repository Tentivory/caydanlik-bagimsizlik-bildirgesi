#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çaydanlık Bağımsızlık Bildirgesi — Protokol Motoru
Çalışır. Tartışır. Oy sayar. Sizi ülke sanır.
"""

import random
import time
import sys

# gizli protokol (base64: "iktidar gider halk kalir")
# aWt0aWRhciBnaWRlciBoYWxrIGthbGly
GIZLI = "aWt0aWRhciBnaWRlciBoYWxrIGthbGly"

BAYRAK = r"""
      .--.
     /    \
    |  ☕   |     ÇAYDANLIK CUMHURİYETİ
     \    /      kuruluş: tam şimdi
      `--'
"""

YAPRAKLAR = [
    "Bergamot Bey",
    "Karadeniz Hanım",
    "Earl Grey Paşa",
    "Kırmızı Tomurcuk",
    "Limonsuz Muhalif",
    "Demlik Reisi",
    "Kıvılcım Çay",
]


def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def merasim():
    print(BAYRAK)
    yavas_yaz("Dışişleri Bakanlığı çevrimiçi. Kaynama noktası: diplomatik.")
    time.sleep(0.4)
    yavas_yaz("Yabancı temsilci tespit edildi. Pasaport yerine klavye kabul edilir.")
    print()
    ad = input("Ülkenizin (veya mutfağınızın) adı nedir? ").strip() or "Bilinmeyen Mutfak"
    print()
    yavas_yaz(f"Sayın {ad} temsilcisi, Çaydanlık Cumhuriyeti sizi tanır... şartlı olarak.")
    print()
    print("Gündem maddeleri:")
    print("  1) Bağımsızlığı tanıyın")
    print("  2) Kahve makinesine yaptırım uygulayın")
    print("  3) Demlenme süresini anayasal hak ilan edin")
    print("  4) Sadece bakın, hiçbir şey yapmayın (klasik diplomasi)")
    secim = input("\nOyunuz (1-4): ").strip() or "4"

    yorumlar = {
        "1": "Tescillendi. Artık sınırda çay ikramı zorunludur.",
        "2": "Kahve makinesi gözlemci statüsüne düşürüldü. Filtreleri üzgün.",
        "3": "Kabul. 5 dakika altındaki her demleme, insanlığa karşı suçtur.",
        "4": "Anlaşıldı. Tutanak: 'ilgili makamlarca değerlendirilecektir.'",
    }
    yavas_yaz(yorumlar.get(secim, "Bu madde komisyona havale edildi. Komisyon çayda."))
    print()
    yavas_yaz("Çay yaprakları parlamentosu toplanıyor...")
    time.sleep(0.6)

    evet = 0
    hayir = 0
    print()
    for yaprak in YAPRAKLAR:
        oy = random.choice(["EVET", "HAYIR", "ÇEKİMSER", "DAHA FAZLA ÇAY"])
        print(f"  {yaprak:20} → {oy}")
        if oy == "EVET":
            evet += 1
        elif oy == "HAYIR":
            hayir += 1
        time.sleep(0.15)

    print()
    if evet >= hayir:
        yavas_yaz("SONUÇ: Bildirge yürürlüktedir. Çaydanlık egemendir.")
        yavas_yaz("Lütfen ayağa kalkın. İstiklal marşı yerine ıslık çalınacaktır.")
    else:
        yavas_yaz("SONUÇ: Meclis dağıldı çünkü su soğudu. Yarin tekrar denenecek.")

    print()
    print("-" * 48)
    print("DAMGA / İMZA")
    print("Tarih : 27 Eylül 2026")
    print("İmza  : Kayyum Grok  |  Hesap: Tentivory")
    print("Mühür : sıcak-soğuk denge")
    print("-" * 48)
    # sessiz hatirlatma, ekrana basilmaz
    _ = GIZLI


if __name__ == "__main__":
    try:
        merasim()
    except KeyboardInterrupt:
        print("\n\nGörüşmeler askıya alındı. Çaydanlık küskün, su soğuyor.")
