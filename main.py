import subprocess
import tkinter as tk
from tkinter import messagebox

APPS = [
    "Viber",
    "Google Chrome",
    "ChatGPT",
    "WebStorm",
    "DataGrip",
    "Terminal",
    "Postman",
    "Docker",
]


def open_all_apps() -> None:
    for app in APPS:
        try:
            subprocess.run(
                ["open", "-a", app],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError) as error:
            details = (
                error.stderr.strip()
                if isinstance(error, subprocess.CalledProcessError)
                   and error.stderr
                else str(error)
            )

            messagebox.showerror(
                "Launch Error",
                f"Could not launch {app}.\n\n{details}",
                parent=window,
            )
            return

    window.destroy()


def confirm_launch() -> None:
    confirmed = messagebox.askyesno(
        "Confirm Launch",
        f"Open all {len(APPS)} applications?",
        parent=window,
    )

    if confirmed:
        open_all_apps()


window = tk.Tk()
window.title("Development Setup")
window.geometry("380x390")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Development Setup",
    font=("Arial", 20, "bold"),
)
title.pack(pady=(25, 10))

description = tk.Label(
    window,
    text="The following applications will be opened:",
    font=("Arial", 11),
)
description.pack(pady=5)

app_list = tk.Label(
    window,
    text="\n".join(f"• {app}" for app in APPS),
    font=("Arial", 12),
    justify="left",
)
app_list.pack(pady=10)

launch_button = tk.Button(
    window,
    text="Launch All",
    command=confirm_launch,
    width=20,
    height=2,
    font=("Arial", 12, "bold"),
)
launch_button.pack(pady=15)

window.mainloop()
