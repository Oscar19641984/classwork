"""
GUI Property Manager

This script provides a small Tkinter GUI that allows the user to add multiple
properties of two types: Rental or Sale. For each property, the user can
enter all relevant attributes. Added properties are shown in a list; selecting
an item displays its full details.

Run: `python propertygpt.py`
"""

from dataclasses import dataclass, asdict
import json
import tkinter as tk
from tkinter import ttk, messagebox


@dataclass
class Property:
    propertyName: str
    propertyAddress: str
    ownerName: str
    propertyType: str
    price: str

    def summary(self) -> str:
        return f"{self.propertyName} ({self.propertyType})"

    def details(self) -> str:
        lines = [
            f"Property Name: {self.propertyName}",
            f"Address: {self.propertyAddress}",
            f"Owner: {self.ownerName}",
            f"Type: {self.propertyType}",
            f"Price: {self.price}",
        ]
        return "\n".join(lines)


@dataclass
class PropertyToRent(Property):
    renterName: str
    dateRented: str
    leaseDuration: str

    def details(self) -> str:
        base = super().details()
        extra = [
            f"Renter: {self.renterName}",
            f"Date Rented: {self.dateRented}",
            f"Lease Duration: {self.leaseDuration}",
        ]
        return base + "\n" + "\n".join(extra)


@dataclass
class PropertyForSale(Property):
    buyerName: str
    dateSold: str

    def details(self) -> str:
        base = super().details()
        extra = [
            f"Buyer: {self.buyerName}",
            f"Date Sold: {self.dateSold}",
        ]
        return base + "\n" + "\n".join(extra)


class PropertyApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Property Manager")
        root.geometry("800x450")

        self.properties = []  # list of Property instances

        self._build_ui()

    def _build_ui(self):
        frm = ttk.Frame(self.root, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(frm)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right = ttk.Frame(frm)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Form on left ---
        ttk.Label(left, text="Add / Edit Property", font=(None, 12, "bold")).grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.entry_vars = {}

        labels = [
            ("Property Name", "propertyName"),
            ("Address", "propertyAddress"),
            ("Owner", "ownerName"),
            ("Price", "price"),
        ]

        for i, (lab, key) in enumerate(labels, start=1):
            ttk.Label(left, text=lab + ":").grid(row=i, column=0, sticky=tk.W, pady=4)
            v = tk.StringVar()
            ent = ttk.Entry(left, textvariable=v, width=40)
            ent.grid(row=i, column=1, sticky=tk.W, pady=4)
            self.entry_vars[key] = v

        # property type combobox
        ttk.Label(left, text="Type:").grid(row=5, column=0, sticky=tk.W, pady=4)
        self.type_var = tk.StringVar(value="Rental")
        cb = ttk.Combobox(left, textvariable=self.type_var, values=["Rental", "Sale"], state="readonly", width=38)
        cb.grid(row=5, column=1, sticky=tk.W, pady=4)
        cb.bind("<<ComboboxSelected>>", lambda e: self._render_type_specific())

        # Type-specific frame
        self.type_frame = ttk.Frame(left)
        self.type_frame.grid(row=6, column=0, columnspan=2, sticky=tk.W)

        # rental fields
        self.renter_var = tk.StringVar()
        self.date_rented_var = tk.StringVar()
        self.lease_var = tk.StringVar()

        ttk.Label(self.type_frame, text="Renter:").grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Entry(self.type_frame, textvariable=self.renter_var, width=30).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(self.type_frame, text="Date Rented:").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Entry(self.type_frame, textvariable=self.date_rented_var, width=30).grid(row=1, column=1, sticky=tk.W)
        ttk.Label(self.type_frame, text="Lease Duration:").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Entry(self.type_frame, textvariable=self.lease_var, width=30).grid(row=2, column=1, sticky=tk.W)

        # sale fields
        self.buyer_var = tk.StringVar()
        self.date_sold_var = tk.StringVar()
        ttk.Label(self.type_frame, text="Buyer:").grid(row=3, column=0, sticky=tk.W, pady=2)
        ttk.Entry(self.type_frame, textvariable=self.buyer_var, width=30).grid(row=3, column=1, sticky=tk.W)
        ttk.Label(self.type_frame, text="Date Sold:").grid(row=4, column=0, sticky=tk.W, pady=2)
        ttk.Entry(self.type_frame, textvariable=self.date_sold_var, width=30).grid(row=4, column=1, sticky=tk.W)

        # Buttons
        btn_frame = ttk.Frame(left)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Add Property", command=self.add_property).pack(side=tk.LEFT, padx=4)
        ttk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=4)
        ttk.Button(btn_frame, text="Export JSON", command=self.export_json).pack(side=tk.LEFT, padx=4)

        # --- Right: list and details ---
        ttk.Label(right, text="Properties", font=(None, 12, "bold")).pack(anchor=tk.W)
        self.listbox = tk.Listbox(right, width=40, height=18)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.listbox.bind("<<ListboxSelect>>", lambda e: self.show_selected_details())

        self.detail_text = tk.Text(right, width=40, height=12, wrap=tk.WORD)
        self.detail_text.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        ttk.Button(right, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=4)
        ttk.Button(right, text="Load Selected Into Form", command=self.load_selected_into_form).pack(side=tk.LEFT, padx=4)

        self._render_type_specific()

    def _render_type_specific(self):
        t = self.type_var.get()
        if t == "Rental":
            # show rental rows 0-2, hide sale rows 3-4
            for i in range(0, 3):
                self.type_frame.grid_rowconfigure(i, minsize=1)
            for i in range(3, 5):
                self.type_frame.grid_rowconfigure(i, minsize=0)
        else:
            for i in range(0, 3):
                self.type_frame.grid_rowconfigure(i, minsize=0)
            for i in range(3, 5):
                self.type_frame.grid_rowconfigure(i, minsize=1)

    def add_property(self):
        name = self.entry_vars['propertyName'].get().strip()
        addr = self.entry_vars['propertyAddress'].get().strip()
        owner = self.entry_vars['ownerName'].get().strip()
        price = self.entry_vars['price'].get().strip()
        ptype = self.type_var.get()

        if not name:
            messagebox.showerror("Missing Field", "Property name is required")
            return

        if ptype == "Rental":
            renter = self.renter_var.get().strip()
            date_rented = self.date_rented_var.get().strip()
            lease = self.lease_var.get().strip()
            prop = PropertyToRent(name, addr, owner, ptype, price, renter, date_rented, lease)
        else:
            buyer = self.buyer_var.get().strip()
            date_sold = self.date_sold_var.get().strip()
            prop = PropertyForSale(name, addr, owner, ptype, price, buyer, date_sold)

        self.properties.append(prop)
        self.listbox.insert(tk.END, prop.summary())
        self.clear_fields()

    def clear_fields(self):
        for v in self.entry_vars.values():
            v.set("")
        self.renter_var.set("")
        self.date_rented_var.set("")
        self.lease_var.set("")
        self.buyer_var.set("")
        self.date_sold_var.set("")

    def show_selected_details(self):
        sel = self.listbox.curselection()
        self.detail_text.delete('1.0', tk.END)
        if not sel:
            return
        idx = sel[0]
        prop = self.properties[idx]
        self.detail_text.insert(tk.END, prop.details())

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.listbox.delete(idx)
        del self.properties[idx]
        self.detail_text.delete('1.0', tk.END)

    def load_selected_into_form(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        prop = self.properties[idx]
        self.entry_vars['propertyName'].set(prop.propertyName)
        self.entry_vars['propertyAddress'].set(prop.propertyAddress)
        self.entry_vars['ownerName'].set(prop.ownerName)
        self.entry_vars['price'].set(prop.price)
        self.type_var.set(prop.propertyType)
        if isinstance(prop, PropertyToRent):
            self.renter_var.set(prop.renterName)
            self.date_rented_var.set(prop.dateRented)
            self.lease_var.set(prop.leaseDuration)
            self.buyer_var.set("")
            self.date_sold_var.set("")
        elif isinstance(prop, PropertyForSale):
            self.buyer_var.set(prop.buyerName)
            self.date_sold_var.set(prop.dateSold)
            self.renter_var.set("")
            self.date_rented_var.set("")
            self.lease_var.set("")
        self._render_type_specific()

    def export_json(self):
        arr = []
        for p in self.properties:
            d = asdict(p)
            arr.append(d)
        try:
            with open('properties_export.json', 'w', encoding='utf-8') as f:
                json.dump(arr, f, indent=2)
            messagebox.showinfo('Export', 'Exported to properties_export.json')
        except Exception as e:
            messagebox.showerror('Export Failed', str(e))


def main():
    root = tk.Tk()
    app = PropertyApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()