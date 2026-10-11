# ad soyad duhan goksal
# ogrenci numarasi 20253004040
# tarih 11 10 2026
# saf fonksiyonlar testleri

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


# envanter_metni testleri

def test_envanter_hepsi_var():
    sonuc = envanter_metni(True, True, True)
    assert sonuc == "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"


def test_envanter_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_kredi_ve_pilot():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_sadece_motor():
    assert envanter_metni(False, True, False) == "Sende: güçlü motorlar"


def test_envanter_sadece_kredi():
    assert envanter_metni(True, False, False) == "Sende: bol kredi"


def test_envanter_sadece_pilot():
    assert envanter_metni(False, False, True) == "Sende: yetenekli bir pilot"


def test_envanter_str_donuyor():
    # saf fonksiyon oldugu icin print degil str donmeli
    sonuc = envanter_metni(True, True, True)
    assert isinstance(sonuc, str)


# hedef_menusu testleri

def test_hedef_tek():
    sonuc = hedef_menusu(["centauri"])
    assert "Nereye gitmek istersin?" in sonuc
    assert "[1] centauri" in sonuc


def test_hedef_iki():
    sonuc = hedef_menusu(["centauri", "sirius"])
    satirlar = sonuc.split("\n")
    assert satirlar[0] == "Nereye gitmek istersin?"
    assert satirlar[1] == "[1] centauri"
    assert satirlar[2] == "[2] sirius"


def test_hedef_bos():
    sonuc = hedef_menusu([])
    assert sonuc == "Nereye gitmek istersin?"


def test_hedef_uc_tane():
    sonuc = hedef_menusu(["a", "b", "c"])
    assert "[1] a" in sonuc
    assert "[2] b" in sonuc
    assert "[3] c" in sonuc
