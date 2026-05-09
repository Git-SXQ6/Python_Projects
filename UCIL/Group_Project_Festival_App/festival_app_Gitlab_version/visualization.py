import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Visualization:
    def __init__(self, parent, data_handler):
        self.parent = parent
        self.data_handler = data_handler
        self.canvas = None
        self.figure = None

    def clear_chart(self):
        """Remove the current chart from the GUI and close the figure."""
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        if self.figure:
            plt.close(self.figure)
            self.figure = None

    def update_graphs(self, ticket_type):
        """Updates and displays graphs based on the selected ticket type."""
        self.clear_chart()

        distribution = self.data_handler.get_distribution_by_accommodation(ticket_type)

        self.figure, ax = plt.subplots()

        if not distribution:
            ax.text(
                0.5, 0.5,
                f"No data available for {ticket_type}",
                ha="center", va="center", fontsize=12
            )
            ax.set_title(f"Accommodation Distribution for {ticket_type} Ticket Holders")
            ax.axis("off")
        else:
            labels = list(distribution.keys())
            sizes = list(distribution.values())
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title(f"Accommodation Distribution for {ticket_type} Ticket Holders")

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)