import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    """Translates the input text into the selected target language."""
    text = text_input.get("1.0", tk.END).strip()
    target_lang = lang_combo.get()
    
    if not text:
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    # Get the correct language code
    target_lang_code = None
    for code, name in LANGUAGES.items():
        if name.lower() == target_lang.lower():
            target_lang_code = code
            break

    if not target_lang_code:
        messagebox.showerror("Error", "Invalid target language.")
        return

    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang_code).text
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")
root.configure(bg="#DDA0DD")  # Light purple background

# Title Label
tk.Label(root, text="Language Translator", font=("Arial", 16, "bold"), bg="#DDA0DD").pack(pady=10)

# Text Input
tk.Label(root, text="Enter Text:", bg="#DDA0DD").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack(pady=5)

# Language Selection
tk.Label(root, text="Select Target Language:", bg="#DDA0DD").pack()
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly")
lang_combo.pack()
lang_combo.set("english")  # Default language selection

# Translate Button
tk.Button(root, text="Translate", command=translate_text, bg="#9370DB", fg="white").pack(pady=10)

# Output Text
tk.Label(root, text="Translated Text:", bg="#DDA0DD").pack()
text_output = tk.Text(root, height=5, width=50)
text_output.pack(pady=5)

root.mainloop()
