# -*- coding: utf-8 -*-
import math
from unittest import TestCase
from scripts.circulo import Circulo


class TestCirculo(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.fig = Circulo()

    def test_get_area(self):
        self.fig.raio = 2
        area = math.pi * self.fig.raio ** 2
        self.assertEqual(self.fig.get_area(), area)

        self.fig.raio = 7.0
        area = math.pi * self.fig.raio ** 2
        self.assertEqual(self.fig.get_area(), area)

    def test_get_perimetro(self):
        self.fig.raio = 2
        perimetro = 2 * math.pi * self.fig.raio
        self.assertEqual(self.fig.get_perimetro(), perimetro)

        self.fig.raio = 7.0
        perimetro = 2 * math.pi * self.fig.raio
        self.assertEqual(self.fig.get_perimetro(), perimetro)
