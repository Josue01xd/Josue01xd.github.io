import tkinter as tk
from tkinter import messagebox

class Vuelo:
    def __init__(self, id_vuelo, origen, destino, fecha, precio):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio
        self.reservado = False

    def __str__(self):
        return f"Vuelo {self.id_vuelo}: {self.origen} a {self.destino}, {self.fecha}, Precio: ${self.precio}"

class SistemaReservas:
    def __init__(self):
        self.vuelos = [
            Vuelo(1, "Madrid", "Barcelona", "2024-12-01", 100),
            Vuelo(2, "Madrid", "Sevilla", "2024-12-05", 90),
            Vuelo(3, "Barcelona", "Valencia", "2024-12-10", 75),
            Vuelo(4, "Madrid", "Bilbao", "2024-12-15", 120),
        ]
        self.reservas = []

    def obtener_vuelos_disponibles(self):
        return [vuelo for vuelo in self.vuelos if not vuelo.reservado]

    def reservar_vuelo(self, vuelo_id):
        for vuelo in self.vuelos:
            if vuelo.id_vuelo == vuelo_id and not vuelo.reservado:
                vuelo.reservado = True
                self.reservas.append(vuelo)
                return vuelo
        return None

    def obtener_reservas(self):
        return self.reservas

class AplicacionReservaVuelos:
    def __init__(self, root):
        self.sistema = SistemaReservas()
        self.root = root
        self.root.title("Sistema de Reserva de Vuelos")
        
        # Etiquetas
        self.titulo = tk.Label(root, text="Bienvenido al Sistema de Reserva de Vuelos", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Listbox de vuelos disponibles
        self.lista_vuelos = tk.Listbox(root, width=50, height=10)
        self.lista_vuelos.pack(pady=10)

        # Botones
        self.boton_reservar = tk.Button(root, text="Reservar vuelo", command=self.reservar_vuelo)
        self.boton_reservar.pack(pady=5)

        self.boton_mostrar_reservas = tk.Button(root, text="Mostrar reservas", command=self.mostrar_reservas)
        self.boton_mostrar_reservas.pack(pady=5)

        self.boton_salir = tk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack(pady=5)

        # Inicializamos la interfaz
        self.actualizar_lista_vuelos()

    def actualizar_lista_vuelos(self):
        # Limpiamos la lista y añadimos los vuelos disponibles
        self.lista_vuelos.delete(0, tk.END)
        vuelos_disponibles = self.sistema.obtener_vuelos_disponibles()
        for vuelo in vuelos_disponibles:
            self.lista_vuelos.insert(tk.END, str(vuelo))

    def reservar_vuelo(self):
        try:
            # Obtener el vuelo seleccionado
            vuelo_seleccionado = self.lista_vuelos.curselection()
            if not vuelo_seleccionado:
                messagebox.showwarning("Selección inválida", "Por favor, selecciona un vuelo.")
                return
            vuelo_id = self.sistema.obtener_vuelos_disponibles()[vuelo_seleccionado[0]].id_vuelo
            vuelo_reservado = self.sistema.reservar_vuelo(vuelo_id)
            
            if vuelo_reservado:
                messagebox.showinfo("Reserva exitosa", f"¡Reserva exitosa! Has reservado el vuelo: {vuelo_reservado}")
                self.actualizar_lista_vuelos()
            else:
                messagebox.showwarning("Vuelo no disponible", "El vuelo seleccionado ya ha sido reservado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def mostrar_reservas(self):
        reservas = self.sistema.obtener_reservas()
        if reservas:
            reservas_texto = "\n".join([str(reserva) for reserva in reservas])
            messagebox.showinfo("Reservas realizadas", reservas_texto)
        else:
            messagebox.showinfo("Sin reservas", "No hay reservas realizadas aún.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionReservaVuelos(root)
    root.mainloop()
