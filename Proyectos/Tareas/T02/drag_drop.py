from PyQt5.QtWidgets import (QLabel, QApplication)
from PyQt5.QtCore import pyqtSignal, QSize, Qt, QMimeData, QTimer
from PyQt5.QtGui import (QPixmap, QDrag)
import parametros_generales as pg
import parametros_plantas as plantas
from os.path import join

# Los qtimer se paran pero se reinician al despausar, no existe un metodo de qtimer para continuar


class ItemDespawneable(QLabel):

    despawn_signal = pyqtSignal(tuple)

    def __init__(self, valor, posicion, parent):
        super().__init__(parent)
        self.valor = valor
        self.posicion = posicion
        self.reloj_interno = QTimer()
        if self.valor == "oro":
            self.reloj_interno.setInterval(pg.DURACION_ORO * 1000)
        else:
            self.reloj_interno.setInterval(pg.DURACION_LENA * 1000)
        self.reloj_interno.timeout.connect(self.despawnear)
        self.reloj_interno.start()

    def despawnear(self):
        self.despawn_signal.emit(self.posicion)


# https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5


class ItemDraggable(QLabel):
    def __init__(self, valor, posicion, parent):
        super().__init__(parent)
        self.valor = valor
        self.posicion = posicion
        self.fondo_item = QPixmap(pg.PATH_TIENDA[self.valor]).scaled(QSize(pg.N * 1, pg.N * 1))
        self.setPixmap(self.fondo_item)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if ((event.pos() - self.drag_start_position).manhattanLength() <
QApplication.startDragDistance()):
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.valor = self.valor
        mimedata.posicion = self.posicion
        mimedata.setImageData(self.pixmap().toImage())
        drag.setMimeData(mimedata)
        drag.setPixmap(self.fondo_item)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)


class LugarDrop(QLabel):

    gasto_item_signal = pyqtSignal(list)

    def __init__(self, text, y, x, parent):
        super().__init__(text, parent)
        self.posicion = (y, x)
        self.setAcceptDrops(True)
        self.plantado = False
        self.stage_actual = 0
        self.stage_max = 1

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            self.stage_actual = 1
            self.valor = event.mimeData().valor
            posicion = event.mimeData().posicion
            self.reloj_interno = QTimer()
            if self.valor == "seed_c":
                self.setText("seed_c")
                self.stage_max = plantas.FASES_CHOCLOS
                self.path = plantas.PATH_SPRITES_CHOCLOS
                self.reloj_interno.setInterval(plantas.TIEMPO_CHOCLOS * 1000)
            else:
                self.setText("seed_a")
                self.stage_max = plantas.FASES_ALCACHOFAS
                self.path = plantas.PATH_SPRITES_ALCACHOFAS
                self.reloj_interno.setInterval(plantas.TIEMPO_ALCACHOFAS * 1000)
            self.final_path = "stage_" + str(self.stage_actual) + ".png"
            self.semilla = QPixmap(join(self.path, self.final_path)).scaled(QSize(pg.N, pg.N))
            self.setPixmap(self.semilla)
            self.setAcceptDrops(False)
            self.plantado = True
            self.reloj_interno.timeout.connect(self.crecer_planta)
            self.reloj_interno.start()
            self.gasto_item_signal.emit([self.valor, posicion])

    def crecer_planta(self):
        self.stage_actual += 1
        if self.stage_actual > self.stage_max:
            self.stage_actual = self.stage_max
        else:
            self.final_path = "stage_" + str(self.stage_actual) + ".png"
            self.planta = QPixmap(join(self.path, self.final_path)).scaled(QSize(pg.N, pg.N))
            self.setPixmap(self.planta)

# Recoger antes de cosechar los choclos, sino se sobreescribe un fruto y queda para siempre

    def cosechar(self):
        if self.valor == "seed_c":
            self.stage_actual -= 1
            self.final_path = "stage_" + str(self.stage_actual) + ".png"
            self.planta = QPixmap(join(self.path, self.final_path)).scaled(QSize(pg.N, pg.N))
            self.setPixmap(self.planta)
        else:
            self.setAcceptDrops(True)
            self.plantado = False
            self.stage_actual = 0
            self.stage_max = 1
            campo = QPixmap(pg.PATH_MAPA["C"]).scaled(QSize(pg.N, pg.N))
            self.setPixmap(campo)
            self.reloj_interno.stop()
