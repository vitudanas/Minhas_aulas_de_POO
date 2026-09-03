import pygame
from dataclasses import dataclass
from enum import Enum, auto
LARGURA, ALTURA = 1000, 600
LINHA_PARADA = 720
PASSO = 0.05
class CorSemaforo(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()
DURACOES = {
    CorSemaforo.VERDE: 6.0,
    CorSemaforo.AMARELO: 1.5,
    CorSemaforo.VERMELHO: 5.0,
}
PROXIMA = {
    CorSemaforo.VERDE: CorSemaforo.AMARELO,
    CorSemaforo.AMARELO: CorSemaforo.VERMELHO,
    CorSemaforo.VERMELHO: CorSemaforo.VERDE,
}
@dataclass
class Semaforo:
        cor: CorSemaforo = CorSemaforo.VERDE
        restante: float = DURACOES[CorSemaforo.VERDE]
    def atualizar(self, dt: float) -> None:
        self.restante -= dt
        if self.restante <= 0:
            self.cor = PROXIMA[self.cor]
            self.restante = DURACOES[self.cor]
    def exige_parada(self) -> bool:
         return self.cor is not CorSemaforo.VERDE