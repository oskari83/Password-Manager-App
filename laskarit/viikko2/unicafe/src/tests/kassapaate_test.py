import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)

    def test_paatteen_saldo_aluksi_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_paatteen_myydyt_aluksi_oikein(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_paatteen_kateisosto_edullinen_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_paatteen_kateisosto_maukas_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_paatteen_kateisosto_edullinen_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_paatteen_kateisosto_maukas_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_paatteen_korttiosto_edullinen_onnistuu(self):
        status = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(status, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_paatteen_korttiosto_edullinen_epaonnistuu(self):
        status = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(status, False)
        self.assertEqual(self.maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_paatteen_korttiosto_maukas_onnistuu(self):
        status = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(status, True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_paatteen_korttiosto_maukas_epaonnistuu(self):
        status = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(status, False)
        self.assertEqual(self.maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus_onnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,200)
        self.assertEqual(self.maksukortti.saldo, 1200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_kortin_lataus_negatiivisellasummalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

   