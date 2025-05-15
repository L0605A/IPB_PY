#!/usr/bin/env python3
from Bio import Entrez, SeqIO
import matplotlib.pyplot as plt, csv

def main():
    e, k, t = input("Mail: "), input("API: "), input("TaxID: ")
    a, b, m = map(int, [input("Min length: "), input("Max length: "), input("Max records: ")])
    Entrez.email, Entrez.api_key, Entrez.tool = e, k, 'Bio'
    try:
        print(f"Searching ID: {t}")
        o = Entrez.read(Entrez.efetch(db="taxonomy", id=t, retmode="xml"))[0]["ScientificName"]
        d = Entrez.read(Entrez.esearch(db="nucleotide", term=f"txid{t}[Organism]", usehistory="y"))
        w, q, c = d["WebEnv"], d["QueryKey"], int(d["Count"])
        print(f"{o}: {c} records found.")
    except: return
    print("Fetching"); r, i = [], 0
    while len(r) < m and i < c:
        h = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", retstart=i, retmax=500, webenv=w, query_key=q)
        for x in SeqIO.parse(h, "genbank"):
            l = len(x.seq)
            if a <= l <= b: r.append((x.id, l, x.description))
            if len(r) >= m: break
        i += 500
    if not r: return
    print(f"Filtered: {len(r)} records.")
    f = f"taxid_{t}"
    with open(f"{f}_report.csv", "w", newline='') as z: csv.writer(z).writerows([["Acc", "Len", "Desc"]] + r)
    print(f"CSV saved: {f}_report.csv")
    r.sort(key=lambda x: -x[1]); x, y = zip(*[(i, l) for i, l, _ in r])
    plt.figure(figsize=(10,5)); plt.plot(x, y, 'o'); plt.xticks(rotation=90, fontsize=6)
    plt.xlabel("Accession"); plt.ylabel("Length"); plt.title("Sequence Lengths")
    plt.tight_layout(); plt.savefig(f"{f}_plot.png"); print(f"Plot saved: {f}_plot.png")

if __name__ == "__main__": main()