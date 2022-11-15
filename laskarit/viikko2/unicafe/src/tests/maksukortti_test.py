import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_aluksi_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortin_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(self.maksukortti.saldo, 1200)

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo, 800)

    def test_rahan_maara_ei_muutu_jos_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_palauttaa_true(self):
        val = self.maksukortti.ota_rahaa(200)
        self.assertEqual(val, True)

    def test_rahan_ottaminen_palauttaa_false(self):
        val = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(val, False)
