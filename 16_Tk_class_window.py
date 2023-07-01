import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")

        self.label = tk.Label(self.root, text="Welcome to My App!")
        self.label.pack(pady=10)

        self.close_button = tk.Button(self.root, text="Close App", command=self.close_app)
        self.close_button.pack(pady=5)

    def close_app(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
