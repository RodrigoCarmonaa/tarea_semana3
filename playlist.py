import random
import time

MAX_CANCIONES = 100
MAX_LONGITUD_NOMBRE = 100

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre[:MAX_LONGITUD_NOMBRE]
        self.canciones = [""] * MAX_CANCIONES
        self.estado = ""
        self.indiceReproduccion = -1
        self.totalCanciones = 0

    def agregarCancion(self, cancion):
        if self.totalCanciones < MAX_CANCIONES:
            self.totalCanciones += 1
            self.canciones[self.totalCanciones - 1] = cancion[:MAX_LONGITUD_NOMBRE]
            return True
        return False

    def eliminarCancion(self, indice):
        if 0 <= indice < self.totalCanciones:
            for i in range(indice, self.totalCanciones - 1):
                self.canciones[i] = self.canciones[i + 1]
            self.totalCanciones -= 1
            return True
        return False

    def mostrarCanciones(self):
        print("Canciones en la playlist:")
        for i, cancion in enumerate(self.canciones[:self.totalCanciones]):
            print(f"{i + 1}. {cancion}")

    def reproducirCancion(self, indice):
        if 0 <= indice < self.totalCanciones:
            self.indiceReproduccion = indice
            self.cambiarEstado("Reproduciendo")

    def seleccionarCancion(self, indice):
        if 0 <= indice < self.totalCanciones:
            self.indiceReproduccion = indice

    def pausar(self):
        self.cambiarEstado("Pausa")

    def detener(self):
        self.cambiarEstado("Detenido")
        self.indiceReproduccion = -1

    def siguienteCancion(self):
        if self.indiceReproduccion < self.totalCanciones - 1:
            self.indiceReproduccion += 1
        else:
            self.detener()

    def cancionAnterior(self):
        if self.indiceReproduccion > 0:
            self.indiceReproduccion -= 1
        else:
            self.detener()

    def reproducirAleatoria(self):
        if self.totalCanciones > 0:
            random.seed(time.time())
            indiceAleatorio = random.randint(0, self.totalCanciones - 1)
            self.reproducirCancion(indiceAleatorio)

    def verEstado(self):
        print(f"Nombre de la playlist: {self.nombre}")
        print(f"Estado: {self.estado}")
        print(f"Índice de reproducción: {self.indiceReproduccion}")
        self.mostrarCanciones()

    def verCancionReproduciendo(self):
        if 0 <= self.indiceReproduccion < self.totalCanciones:
            print(f"Canción reproduciéndose: {self.canciones[self.indiceReproduccion]}")
        else:
            print("Ninguna canción reproduciéndose.")

    def cambiarEstado(self, nuevoEstado):
        self.estado = nuevoEstado[:MAX_LONGITUD_NOMBRE]

def main():
    miPlaylist = Playlist("Mi Playlist")

    opcion = None
    indice = None
    cancion = ""

    while opcion != 0:
        print("\n=== Menú de la Playlist ===")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Mostrar todas las canciones")
        print("4. Reproducir canción")
        print("5. Seleccionar canción")
        print("6. Pausar")
        print("7. Detener")
        print("8. Siguiente canción")
        print("9. Canción anterior")
        print("10. Reproducir canción aleatoria")
        print("11. Ver estado de la playlist")
        print("12. Ver canción reproduciéndose")
        print("0. Salir")
        
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cancion = input("Ingrese el nombre de la canción a agregar: ")
            if miPlaylist.agregarCancion(cancion):
                print("Canción agregada exitosamente.")
            else:
                print("La playlist está llena. No se pudo agregar la canción.")
        elif opcion == 2:
            indice = int(input("Ingrese el índice de la canción a eliminar: "))
            if miPlaylist.eliminarCancion(indice - 1):
                print("Canción eliminada exitosamente.")
            else:
                print("Índice no válido. No se pudo eliminar la canción.")
        elif opcion == 3:
            miPlaylist.mostrarCanciones()
        elif opcion == 4:
            indice = int(input("Ingrese el índice de la canción a reproducir: "))
            miPlaylist.reproducirCancion(indice - 1)
        elif opcion == 5:
            indice = int(input("Ingrese el índice de la canción a seleccionar: "))
            miPlaylist.seleccionarCancion(indice - 1)
        elif opcion == 6:
            miPlaylist.pausar()
        elif opcion == 7:
            miPlaylist.detener()
        elif opcion == 8:
            miPlaylist.siguienteCancion()
        elif opcion == 9:
            miPlaylist.cancionAnterior()
        elif opcion == 10:
            miPlaylist.reproducirAleatoria()
        elif opcion == 11:
            miPlaylist.verEstado()
        elif opcion == 12:
            miPlaylist.verCancionReproduciendo()
        elif opcion == 0:
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
