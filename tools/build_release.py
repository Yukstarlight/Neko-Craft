import os, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "1.0.0"
ADAPTED = [
    "toneko-fabric-1.9.7.jar",
    "JustARod-0.2.2.jar",
    "theartofstockings-0.11.0.jar",
    "justarod-attrfix-neoforge-1.0.2.jar",
]
DOCS = ["README.md", "LICENSE", "docs/MODS.md"]

mods_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "mods")
missing = [f for f in ADAPTED if not os.path.isfile(os.path.join(mods_dir, f))]
if missing:
    sys.exit("缺少本地适配构建：" + ", ".join(missing))

out_dir = os.path.join(ROOT, "dist")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, f"Neko-Craft-{VERSION}.zip")
prefix = f"Neko-Craft-{VERSION}/"

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name in DOCS:
        z.write(os.path.join(ROOT, name), prefix + name)
    for tree in ("config", "ctlib"):
        base = os.path.join(ROOT, tree)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(dirnames)
            for name in sorted(filenames):
                src = os.path.join(dirpath, name)
                rel = os.path.relpath(src, ROOT).replace(os.sep, "/")
                z.write(src, prefix + rel)
    for name in ADAPTED:
        z.write(os.path.join(mods_dir, name), prefix + "mods/" + name)
    entries = len(z.namelist())

print(f"built {out} ({os.path.getsize(out)} bytes, {entries} entries)")
